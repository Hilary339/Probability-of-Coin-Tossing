# Coin Toss Frequency Visualization

This repository contains three Python scripts that simulate coin tossing and visualize how the frequency of heads approaches 0.5 as the number of tosses increases (the law of large numbers). Each script uses a different approach to generate random samples and compute cumulative frequencies.

## Scripts Overview

| Script | Method | Description |
|--------|--------|-------------|
| `coin_loop.py` | Python `for` loop + `random.random()` | Simulates tosses one by one in a loop. Simplest to read but slowest for large `N`. |
| `coin_numpy.py` | NumPy vectorized operations | Generates all tosses at once using `np.random.choice` and computes cumulative sums with `np.cumsum`. Fast and concise. |
| `coin_torch.py` | PyTorch tensor operations | Uses `torch.multinomial` for sampling and `cumsum(dim=0)` for accumulation. Can leverage GPU if available. Best for very large `N` or deep learning pipelines. |

## Requirements

- Python 3.6+
- Matplotlib (for plotting)
- NumPy (for the NumPy script)
- PyTorch (for the PyTorch script)

Install the dependencies with:

```bash
pip install matplotlib numpy torch
```
## How to Run

Each script is self-contained. Run any of them with Python:

```bash
python coin_loop.py
python coin_numpy.py
python coin_torch.py
```
Each script will display a plot showing the estimated probability of heads (frequency) vs. the number of tosses, with a dashed horizontal line at 0.5 for reference. The x‑axis uses a logarithmic scale to highlight early fluctuations.

## Key Differences

Speed: For N = 100,000, all three run within a fraction of a second. For N = 10,000,000, the loop version slows down significantly, while NumPy and PyTorch remain fast. PyTorch can be even faster on a GPU.
Readability: The loop version is the most intuitive for beginners. The NumPy version offers a good balance of speed and simplicity. The PyTorch version uses tensor operations and is familiar to deep learning practitioners.
Output: All three produce the same type of plot, but the PyTorch script also demonstrates how to compute cumulative frequencies using cumsum(dim=0) and one‑hot encoding (optional).

## Example Output

The plot shows the frequency of heads starting from 0 or 1, then rapidly converging to 0.5 as the number of tosses grows.
