import os
import json
import pandas as pd
from dotenv import load_dotenv
from dune_client.client import DuneClient
from dune_client.query import QueryBase

load_dotenv()
api_key = os.getenv("DUNE_API")
dune = DuneClient(api_key=api_key)

# Load query mapping
with open("queries.json", "r") as f:
    QUERIES = json.load(f)

def fetch_data(protocol: str, metric: str) -> pd.DataFrame:
    query_id = QUERIES[protocol][metric]
    query = QueryBase(query_id=query_id)
    results = dune.run_query(query)
    rows = results.result.rows
    return pd.DataFrame(rows)
