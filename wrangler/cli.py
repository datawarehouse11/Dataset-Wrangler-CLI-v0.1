# wrangler/cli.py
import argparse
from wrangler.io import load_dataset, save_dataset
from wrangler.cleaning import drop_duplicates, impute_column
from wrangler.encoding import apply_mappings

def parse_encode_arg(arg):
    # e.g., "gender:male=0,female=1"
    mappings = {}
    if not arg:
        return mappings
    for spec in arg:
        col, pairs = spec.split(":")
        kv = {}
        for p in pairs.split(","):
            k, v = p.split("=")
            kv[k] = int(v)
        mappings[col] = kv
    return mappings

def run_cli():
    parser = argparse.ArgumentParser(description="Dataset Wrangler CLI v0.1")
    parser.add_argument("--input", required=True, help="Path to input CSV/JSON")
    parser.add_argument("--output", required=True, help="Path to save cleaned dataset")
    parser.add_argument("--impute", default="median", choices=["median", "mean", "mode", "none"],
                        help="Imputation strategy for numeric columns")
    parser.add_argument("--encode", nargs="*", help="Categorical mappings: col:a=0,b=1")
    parser.add_argument("--drop-duplicates", action="store_true", default=True,
                        help="Drop duplicate rows (default: True)")
    args = parser.parse_args()

    df = load_dataset(args.input)

    if args.drop_duplicates:
        df = drop_duplicates(df)

    # Impute numeric columns
    if args.impute != "none":
        for col in df.select_dtypes(include=["float64", "int64"]).columns:
            df[col] = impute_column(df[col], strategy=args.impute)

    # Apply categorical mappings
    mappings = parse_encode_arg(args.encode)
    if mappings:
        df = apply_mappings(df, mappings)

    save_dataset(df, args.output)
    print(f"[v0.1] Saved cleaned dataset to: {args.output}")
