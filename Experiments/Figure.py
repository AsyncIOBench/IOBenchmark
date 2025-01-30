import pandas as pd
import matplotlib.pyplot as plt

data = {
    "Engine": ["libaio", "libaio", "io_uring", "io_uring", "SPDK", "SPDK"],
    "Test Type": ["Rand Read", "Rand Write", "Rand Read", "Rand Write", "Rand Read", "Rand Write"],
    "IOPS": [2583, 1839, 1016, 1866, 258000, 517000],
    "Latency (µs)": [378.95, 523.40, 970.34, 521.96, 1.64, 1.61],
    "Bandwidth (MiB/s)": [10.1, 7.3, 4.1, 7.5, 1007, 2018]
}

df = pd.DataFrame(data)

fig, axs = plt.subplots(3, 1, figsize=(10, 12))

axs[0].bar(df["Engine"] + " - " + df["Test Type"], df["IOPS"], color="lightblue")
axs[0].set_title("IOPS Comparison")
axs[0].set_ylabel("IOPS (Ops/sec)")
axs[0].tick_params(axis='x', rotation=45)

axs[1].bar(df["Engine"] + " - " + df["Test Type"], df["Latency (µs)"], color="orange")
axs[1].set_title("Latency Comparison")
axs[1].set_ylabel("Latency (µs)")
axs[1].tick_params(axis='x', rotation=45)

axs[2].bar(df["Engine"] + " - " + df["Test Type"], df["Bandwidth (MiB/s)"], color="green")
axs[2].set_title("Bandwidth Comparison")
axs[2].set_ylabel("Bandwidth (MiB/s)")
axs[2].tick_params(axis='x', rotation=45)

plt.tight_layout()
plt.savefig("Figure.png", dpi=300)
plt.show()

print(df)