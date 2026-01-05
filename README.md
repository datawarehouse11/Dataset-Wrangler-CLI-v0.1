# Dataset-Wrangler-CLI-v0.1
A lightweight Python command‑line tool for cleaning, imputing, and encoding datasets. Built for visibility and portfolio growth — proving end‑to‑end execution from raw data to cleaned output.

# Dataset Wrangler CLI v0.1

This is an end‑to‑end dataset cleaning tool, built as a command‑line interface in Python.  
The goal was simple: prove I can ship a working artifact that takes raw data, cleans it, and saves the result — all visible, testable, and defensible.

---

## What It Does
- Load datasets from **CSV** or **JSON**
- Drop duplicate rows
- Impute missing numeric values (median, mean, mode, or none)
- Encode categorical variables with custom mappings
- Save the cleaned dataset back to disk
- Includes smoke tests to validate the basics

---

## Project Layout
'''
dataset-wrangler/
├─ wrangler/
│  ├─ io.py           # load/save datasets
│  ├─ cleaning.py     # drop duplicates + impute
│  ├─ encoding.py     # apply categorical mappings
│  └─ cli.py          # CLI orchestration
├─ tests/
│  └─ test_smoke.py  # sanity checks for cleaning + encoding
├─ examples/
│  └─ sample.csv      # demo dataset
├─ main.py            # entry point
├─ requirements.txt   # dependencies
└─ README.md          # documentation
'''

## Installation
Clone the repo and install dependencies:
```bash
git clone https://github.com/<my-username>/dataset-wrangler-cli.git
cd dataset-wrangler-cli
pip install -r requirements.txt

Usage
Run the CLI:
python main.py \
  --input examples/sample.csv \
  --output cleaned.csv \
  --impute median \
  --encode gender:male=0,female=1 \
  --drop-duplicates

Testing
I added smoke tests to prove the basics work. Run them with:
pytest

Example output:
============================= test session starts =============================
collected 2 items

tests/test_smoke.py ..                                                [100%]

============================== 2 passed in 0.12s ==============================

Demo Workflow
Input dataset (examples/sample.csv):
id,age,gender
1,34,male
2,,female
3,29,male
3,29,male

Command:
python main.py --input examples/sample.csv --output cleaned.csv --impute median --encode gender:male=0,female=1

Output dataset (cleaned.csv):
id,age,gender
1,34,0
2,31.5,1
3,29,0

Roadmap
- v1.0 → Logging, config file support, benchmarks, expanded tests
- v2.0 → Pipelines + profiling
- v3.0 → Cross‑language ports (Go, TypeScript)
- v4.0 → Agent layer for autonomous dataset wrangling

License
MIT License — free to use, modify, and share.
