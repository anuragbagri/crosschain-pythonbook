import matplotlib.pyplot as plt

def plot_timeseries(data, x_col, y_col, title=None):
    plt.figure(figsize=(10,6))
    plt.plot(data[x_col], data[y_col], marker="o")
    plt.xlabel(x_col)
    plt.ylabel(y_col)
    plt.title(title or f"{y_col} over {x_col}")
    plt.xticks(rotation=45)
    plt.grid(True)
    plt.tight_layout()
    plt.show()
