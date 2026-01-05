<<<<<<< HEAD
# wrangler/encoding.py
import pandas as pd

def apply_mappings(df: pd.DataFrame, mappings: dict) -> pd.DataFrame:
    for col, map_dict in mappings.items():
        if col in df.columns:
            df[col] = df[col].map(map_dict)
    return df
=======
# wrangler/encoding.py
import pandas as pd

def apply_mappings(df: pd.DataFrame, mappings: dict) -> pd.DataFrame:
    for col, map_dict in mappings.items():
        if col in df.columns:
            df[col] = df[col].map(map_dict)
    return df
>>>>>>> 0b980f8 (Initial commit: Dataset Wrangler CLI v0.1)
