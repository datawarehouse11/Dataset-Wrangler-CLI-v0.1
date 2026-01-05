# wrangler/cleaning.py
import pandas as pd

def drop_duplicates(df: pd.DataFrame) -> pd.DataFrame:
    return df.drop_duplicates()

def impute_column(series: pd.Series, strategy: str = "median") -> pd.Series:
    if strategy == "median":
        return series.fillna(series.median())
    elif strategy == "mean":
        return series.fillna(series.mean())
    elif strategy == "mode":
        mode = series.mode()
        return series.fillna(mode.iloc[0] if not mode.empty else series)
    else:
        return series