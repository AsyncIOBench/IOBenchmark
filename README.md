# IOBenchmark

# NVMe Storage Benchmarking

This repository contains scripts and tools for benchmarking NVMe storage using different I/O engines, including `libaio`, `io_uring`, and `SPDK`. It also includes performance analysis and results obtained from running these tests.

## 📂 Repository Structure
- **`Experiments`** - Contains Shell scripts for running benchmarks with different I/O engines, Output files and performance analysis from the benchmarking tests, Installation and testing scripts for SPDK, and Scripts for evaluating RocksDB performance on NVMe storage.
- **`Report/`** - LaTeX source files of the performance analysis report, including detailed results, figures, and discussions.

## Setup and Usage

### Clone the Repository
```bash
git clone https://github.com/AsyncIOBench/IOBenchmark.git
cd IOBenchmark
```

### Run Benchmarking Scripts
Each script runs `fio` with a specific I/O engine:
- `script1.sh` → Uses `libaio`
- `script2.sh` → Uses `io_uring`
- `script3.sh` → Uses `SPDK`

Run a script using:
```bash
chmod +x Experiments/libaio/script1.sh
./Experiments/libaio/script1.sh
```

### View Results
After execution, results are saved in `Experiments`. You can analyze them using:
```bash
cat Experiments/libaio/randwrite_1.txt
```

## Performance Analysis
The repository includes:
- **Latency, IOPS, and Bandwidth comparisons** for `libaio` and `io_uring`.
- **NVMe storage behavior under high load**.
- **SPDK and RocksDB performance testing**.