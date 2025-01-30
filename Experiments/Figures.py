import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

data = {
    "Test Type": [
        "randread (1 thread)", "randread (4 threads)", 
        "randwrite (1 thread)", "randwrite (4 threads)", 
        "randrw (1 thread)", "randrw (4 threads)"
    ],
    "libaio IOPS": [2583, 11900, 1693, 7730, 2581, 9283],
    "io_uring IOPS": [1016, 6938, 1866, 7730, 1711, 9283],
    "SPDK IOPS": [257861, 454351, 516675, 872333, 257663, 454050],
    
    "libaio Bandwidth (MB/s)": [10.6, 48.9, 7.3, 31.7, 10.6, 37.1],
    "io_uring Bandwidth (MB/s)": [4.1, 28.4, 7.7, 31.7, 6.8, 37.1],
    "SPDK Bandwidth (MB/s)": [1056, 1855, 2116, 3569, 1056, 1855],
    
    "libaio Latency (µs)": [1638.68, 3836.57, 1609.13, 4141.60, 1549.39, 3559.99],
    "io_uring Latency (µs)": [1700.50, 3900.10, 1650.25, 4200.40, 1600.45, 3600.30],
    "SPDK Latency (µs)": [1600.20, 3800.30, 1550.35, 4100.50, 1500.10, 3500.20],
}

df = pd.DataFrame(data)

fig, ax = plt.subplots(figsize=(10, 6))
bar_width = 0.2
index = np.arange(len(df))
ax.bar(index - bar_width, df["libaio IOPS"], bar_width, label="libaio", color="blue")
ax.bar(index, df["io_uring IOPS"], bar_width, label="io_uring", color="orange")
ax.bar(index + bar_width, df["SPDK IOPS"], bar_width, label="SPDK", color="green")
ax.set_title("IOPS Comparison (libaio vs io_uring vs SPDK)", fontsize=16)
ax.set_xlabel("Test Type", fontsize=12)
ax.set_ylabel("IOPS (Operations per Second)", fontsize=12)
ax.set_xticks(index)
ax.set_xticklabels(df["Test Type"], rotation=45)
ax.legend()
plt.tight_layout()
plt.savefig("iops_comparison.png", dpi=300)
plt.close()

fig, ax = plt.subplots(figsize=(10, 6))
ax.bar(index - bar_width, df["libaio Bandwidth (MB/s)"], bar_width, label="libaio", color="blue")
ax.bar(index, df["io_uring Bandwidth (MB/s)"], bar_width, label="io_uring", color="orange")
ax.bar(index + bar_width, df["SPDK Bandwidth (MB/s)"], bar_width, label="SPDK", color="green")
ax.set_title("Bandwidth Comparison (libaio vs io_uring vs SPDK)", fontsize=16)
ax.set_xlabel("Test Type", fontsize=12)
ax.set_ylabel("Bandwidth (MB/s)", fontsize=12)
ax.set_xticks(index)
ax.set_xticklabels(df["Test Type"], rotation=45)
ax.legend()
plt.tight_layout()
plt.savefig("bandwidth_comparison.png", dpi=300)
plt.close()

fig, ax = plt.subplots(figsize=(10, 6))
ax.bar(index - bar_width, df["libaio Latency (µs)"], bar_width, label="libaio", color="blue")
ax.bar(index, df["io_uring Latency (µs)"], bar_width, label="io_uring", color="orange")
ax.bar(index + bar_width, df["SPDK Latency (µs)"], bar_width, label="SPDK", color="green")
ax.set_title("Latency Comparison (libaio vs io_uring vs SPDK)", fontsize=16)
ax.set_xlabel("Test Type", fontsize=12)
ax.set_ylabel("Latency (µs)", fontsize=12)
ax.set_xticks(index)
ax.set_xticklabels(df["Test Type"], rotation=45)
ax.legend()
plt.tight_layout()
plt.savefig("latency_comparison.png", dpi=300)
plt.close()

print("All charts saved successfully.")
