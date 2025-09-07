import os
import pandas as pd
from dune_utils import fetch_data, QUERY_IDS

OUTPUT_DIR = "output"
os.makedirs(OUTPUT_DIR, exist_ok=True)

def save_to_csv(protocol, metric):
    df = fetch_data(protocol, metric)
    file_path = f"{OUTPUT_DIR}/{protocol}_{metric}.csv"
    df.to_csv(file_path, index=False)
    print(f"✅ Saved {protocol} - {metric} → {file_path}")

def run_all():
    for protocol in QUERY_IDS:
        for metric in QUERY_IDS[protocol]:
            save_to_csv(protocol, metric)

if __name__ == "__main__":
    # run everything at once
    run_all()
