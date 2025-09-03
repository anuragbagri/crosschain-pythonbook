import argparse
from dune_utils import fetch_data
from plot_utils import plot_timeseries
from plot_volume import plot_volume

def main():
    parser = argparse.ArgumentParser(description="Cross-chain Bridge Analysis")
    parser.add_argument("protocol", choices=["everclear", "stargate", "across", "usdto"], help="Which protocol?")
    parser.add_argument("metric", choices=["volume", "user_growth", "active_users"], help="Which metric?")
    args = parser.parse_args()

    # Fetch data
    data = fetch_data(args.protocol, args.metric)
    print(data.head())

    if args.metric == "volume":
        # Single-column case → line graph with index
        plot_volume(data, args.protocol)
    else:
        # Normal time series
        if data.shape[1] >= 2:
            x_col, y_col = data.columns[0], data.columns[1]
            plot_timeseries(data, x_col, y_col, f"{args.protocol} - {args.metric}")
        else:
            print("⚠️ This metric has no time-series data to plot")

if __name__ == "__main__":
    main()
