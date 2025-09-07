from dune_client.client import DuneClient
from dune_client.query import QueryBase
import os
from dotenv import load_dotenv
import pandas as pd

# Load Dune API key
load_dotenv()
api_key = os.getenv("DUNE_API")
dune = DuneClient(api_key=api_key)

# Query IDs for each protocol & metric
QUERY_IDS = {
  "stargate": {
    "volume": 5619068,
    "user_growth": 5626075,
    "active_users": 5690955
  },
  "everclear": {
    "volume": 5623778,
    "user_growth": 5661231,
    "active_users": 5691028
  },
  "across": {
    "volume": 5623223,
    "user_growth": 5661131,
    "active_users": 5691085
  },
  "hyperliquid": {
    "volume": 5624003,
    "user_growth": 5626531,
    "active_users": 5691000
  }
}

def fetch_data(protocol: str, metric: str) -> pd.DataFrame:
    
    query_id = QUERY_IDS.get(protocol, {}).get(metric)
    if not query_id:
        raise ValueError(f"No query found for protocol={protocol}, metric={metric}")
    query = QueryBase(query_id=query_id)
    results = dune.run_query(query)
    return pd.DataFrame(results.result.rows)
