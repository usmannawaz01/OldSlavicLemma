import argparse
from .trainer import TrainSettings, train_model


def make_parser():
    parser = argparse.ArgumentParser(prog="oldslaviclemma-train")
    sub = parser.add_subparsers(dest="command")

    fit = sub.add_parser("fit")
    fit.add_argument("--train", required=True)
    fit.add_argument("--dev", required=True)
    fit.add_argument("--test", required=True)
    fit.add_argument("--output", required=True)
    fit.add_argument("--model-id", default="model")
    fit.add_argument("--batch-size", type=int, default=32)
    fit.add_argument("--epochs", type=int, default=75)
    fit.add_argument("--lr", type=float, default=1.5e-4)
    fit.add_argument("--weight-decay", type=float, default=3e-5)
    fit.add_argument("--char-emb-dim", type=int, default=96)
    fit.add_argument("--hidden-size", type=int, default=128)
    fit.add_argument("--drop-prob", type=float, default=0.30)
    fit.add_argument("--clip-norm", type=float, default=5.0)
    fit.add_argument("--num-heads", type=int, default=16)
    fit.add_argument("--max-gen-len", type=int, default=30)
    fit.add_argument("--early-stop-patience", type=int, default=15)
    fit.add_argument("--k-context", type=int, default=2)
    fit.add_argument("--sep-char", default="⟂")
    return parser


def run(argv=None):
    parser = make_parser()
    args = parser.parse_args(argv)

    if args.command == "fit":
        settings = TrainSettings(
            train_conllu=args.train,
            dev_conllu=args.dev,
            test_conllu=args.test,
            save_dir=args.output,
            model_id=args.model_id,
            batch_size=args.batch_size,
            epochs=args.epochs,
            lr=args.lr,
            weight_decay=args.weight_decay,
            char_emb_dim=args.char_emb_dim,
            hidden_size=args.hidden_size,
            drop_prob=args.drop_prob,
            clip_norm=args.clip_norm,
            num_heads=args.num_heads,
            max_gen_len=args.max_gen_len,
            early_stop_patience=args.early_stop_patience,
            k_context=args.k_context,
            sep_char=args.sep_char
        )
        train_model(settings)
        return

    parser.print_help()


def main():
    run()


if __name__ == "__main__":
    main()
