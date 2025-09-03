import matplotlib.pyplot as plt

def plot_volume(data, protocol: str):

    if data.shape[1] != 1:
        raise ValueError("Volume query should return exactly one column")

    y_col = data.columns[0]
    plt.figure(figsize=(10,6))
    plt.plot(data.index, data[y_col], marker="o")
    plt.title(f"{protocol} -  Volume (last 30 days)")
    plt.xlabel("Transaction Index")
    plt.ylabel("Volume")
    plt.grid(True)
    plt.tight_layout()
    plt.show()
