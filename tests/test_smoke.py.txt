<<<<<<< HEAD
# test/test_smoke.py
import pandas as pd
from wrangler.cleaning import drop_duplicates, impute_column
from wrangler.encoding import apply_mappings

def test_basic_cleaning():
    df = pd.DataFrame({"a":[1,1,2], "b":[None,2,3]})
    df = drop_duplicates(df)
    assert len(df) == 2
    df["b"] = impute_column(df["b"], "median")
    assert df["b"].isna().sum() == 0

def test_encoding():
    df = pd.DataFrame({"gender":["male","female","male"]})
    df = apply_mappings(df, {"gender":{"male":0,"female":1}})
    assert set(df["gender"].unique()) == {0,1}
=======
# test/test_smoke.py
import pandas as pd
from wrangler.cleaning import drop_duplicates, impute_column
from wrangler.encoding import apply_mappings

def test_basic_cleaning():
    df = pd.DataFrame({"a":[1,1,2], "b":[None,2,3]})
    df = drop_duplicates(df)
    assert len(df) == 2
    df["b"] = impute_column(df["b"], "median")
    assert df["b"].isna().sum() == 0

def test_encoding():
    df = pd.DataFrame({"gender":["male","female","male"]})
    df = apply_mappings(df, {"gender":{"male":0,"female":1}})
    assert set(df["gender"].unique()) == {0,1}
>>>>>>> 0b980f8 (Initial commit: Dataset Wrangler CLI v0.1)
