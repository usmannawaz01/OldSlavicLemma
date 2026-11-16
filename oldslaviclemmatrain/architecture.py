import torch
import torch.nn as nn


class LemmaModel(nn.Module):
    def __init__(self, vocab_size, char_emb_dim=96, hidden_size=128, drop_prob=0.30, num_heads=16, max_gen_len=30):
        super().__init__()
        self.char_emb_dim = char_emb_dim
        self.hidden_size = hidden_size
        self.drop_prob = drop_prob
        self.num_heads = num_heads
        self.max_gen_len = max_gen_len

        self.emb = nn.Embedding(vocab_size, char_emb_dim, padding_idx=0)

        self.dropout_enc = nn.Dropout(drop_prob)
        self.dropout_dec = nn.Dropout(drop_prob)
        self.dropout_att = nn.Dropout(drop_prob)

        self.enc1 = nn.LSTM(char_emb_dim, hidden_size, bidirectional=True, batch_first=True)
        self.enc2 = nn.LSTM(hidden_size * 2, hidden_size, bidirectional=True, batch_first=True)
        self.attn = nn.MultiheadAttention(hidden_size * 2, num_heads, batch_first=True)

        self.dec = nn.LSTM(char_emb_dim + hidden_size * 4, hidden_size * 2, batch_first=True)

        self.dec_cross_attn = nn.MultiheadAttention(
            embed_dim=hidden_size * 2,
            num_heads=num_heads,
            kdim=hidden_size * 4,
            vdim=hidden_size * 4,
            batch_first=True
        )
        self.out = nn.Linear(hidden_size * 2, vocab_size, bias=True)

    def encode(self, src, src_lens):
        emb = self.emb(src)
        packed1 = nn.utils.rnn.pack_padded_sequence(emb, src_lens.cpu(), batch_first=True, enforce_sorted=False)
        enc1_o, _ = self.enc1(packed1)
        enc1_o, _ = nn.utils.rnn.pad_packed_sequence(enc1_o, batch_first=True)
        enc1_o = self.dropout_enc(enc1_o)

        packed2 = nn.utils.rnn.pack_padded_sequence(enc1_o, src_lens.cpu(), batch_first=True, enforce_sorted=False)
        enc2_o, _ = self.enc2(packed2)
        enc2_o, _ = nn.utils.rnn.pad_packed_sequence(enc2_o, batch_first=True)
        enc2_o = self.dropout_enc(enc2_o)

        attn_o, _ = self.attn(enc1_o, enc2_o, enc2_o)
        attn_o = self.dropout_att(attn_o)

        return torch.cat([enc2_o, attn_o], dim=-1)

    def forward(self, src, src_lens, tgt):
        if self.training:
            m = (torch.rand_like(src, dtype=torch.float32) < 0.05) & (src > 3)
            src = torch.where(m, torch.full_like(src, 3), src)

        encoder_combined = self.encode(src, src_lens)
        dt = self.emb(tgt[:, :-1])

        length = dt.size(1)
        if encoder_combined.size(1) >= length:
            comb_trim = encoder_combined[:, :length, :]
        else:
            pad = encoder_combined.new_zeros(
                encoder_combined.size(0),
                length - encoder_combined.size(1),
                encoder_combined.size(2)
            )
            comb_trim = torch.cat([encoder_combined, pad], dim=1)

        dec_inp = torch.cat([dt, comb_trim], dim=-1)
        dec_o, _ = self.dec(dec_inp)
        dec_o = self.dropout_dec(dec_o)

        cross_out, _ = self.dec_cross_attn(dec_o, encoder_combined, encoder_combined)
        cross_out = self.dropout_att(cross_out)

        return self.out(cross_out)

    def generate(self, src, src_lens, vocab, max_len=None):
        self.eval()
        if max_len is None:
            max_len = self.max_gen_len
        batch_size = src.size(0)
        with torch.no_grad():
            encoder_combined = self.encode(src, src_lens)
            src_steps = encoder_combined.size(1)
            cur = torch.full((batch_size, 1), vocab.char2idx["<sos>"], device=src.device, dtype=torch.long)
            hidden = None
            hyps = [[] for _ in range(batch_size)]
            for step in range(max_len):
                emb_t = self.emb(cur).squeeze(1)
                comb_t = encoder_combined[:, 0, :] if src_steps == 0 else encoder_combined[:, min(step, src_steps - 1), :]

                dec_inp_t = torch.cat([emb_t, comb_t], dim=-1).unsqueeze(1)
                dec_o, hidden = self.dec(dec_inp_t, hidden)
                dec_o = self.dropout_dec(dec_o)
                cross_out, _ = self.dec_cross_attn(dec_o, encoder_combined, encoder_combined)
                cross_out = self.dropout_att(cross_out)
                logits = self.out(cross_out)
                cur = logits.argmax(-1)
                for i in range(batch_size):
                    hyps[i].append(int(cur[i, 0].item()))
                if all(int(cur[i, 0].item()) == vocab.char2idx["<eos>"] for i in range(batch_size)):
                    break
        return [vocab.decode(h) for h in hyps]
