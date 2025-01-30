import pandas as pd
import matplotlib.pyplot as plt

data = {
    "Engine": ["libaio", "libaio", "io_uring", "io_uring", "SPDK", "SPDK"],
    "Test Type": ["Rand Read", "Rand Write", "Rand Read", "Rand Write", "Rand Read", "Rand Write"],
    "IOPS": [2583, 1866, 1016, 1866, 258000, 517000],
    "Latency (µs)": [378.95, 523.40, 970.34, 521.96, 1.64, 1.61],
    "Bandwidth (MiB/s)": [10.1, 7.3, 4.1, 7.5, 1007, 2018]
}

df = pd.DataFrame(data)

fig, axs = plt.subplots(3, 1, figsize=(10, 14))

def plot_bar(ax, y_values, title, ylabel, color):
    bars = ax.bar(df["Engine"] + " - " + df["Test Type"], y_values, color=color)
    ax.set_title(title, fontsize=12, pad=10)
    ax.set_ylabel(ylabel, fontsize=10)
    ax.set_xticklabels(df["Engine"] + " - " + df["Test Type"], rotation=20, ha="right", fontsize=9)
    for bar in bars:
        height = bar.get_height()
        ax.annotate(f"{height:.2f}", xy=(bar.get_x() + bar.get_width() / 2, height),
                    xytext=(0, 3), textcoords="offset points",
                    ha="center", fontsize=8, color="black")

plt.subplots_adjust(hspace=0.3)

plot_bar(axs[0], df["IOPS"], "IOPS Comparison", "IOPS", "lightblue")
plot_bar(axs[1], df["Latency (µs)"], "Latency Comparison", "Latency (µs)", "orange")
plot_bar(axs[2], df["Bandwidth (MiB/s)"], "Bandwidth Comparison", "Bandwidth (MiB/s)", "green")

plt.savefig("Overview.png", dpi=300, bbox_inches="tight")
plt.show()