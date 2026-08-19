# Chaos Lab

A small scientific computing playground for exploring nonlinear dynamics, discrete systems, and mathematical visualization.

The first experiment in this repository is a **cobweb plot visualizer** (also known as a Verhulst diagram), which transforms time-series data into a graphical representation of iterative dynamics.

## Overview

Cobweb plots are commonly used to visualize discrete dynamical systems:

$Y_t \rightarrow Y_{t+1}$

They show how a system evolves from one iteration to the next and are often used when studying population models, recurrence relations, and chaotic behavior.

This project takes a time-series dataset, prepares the trajectory, and generates a cobweb diagram with the identity line:

$Y_t = Y_{t+1}$

---
## Features
- Generate cobweb plots from time-series datasets
- Normalize input trajectories for comparative visualization
- Transform raw observations into iterative coordinates
- Display the identity function reference line
- Configurable input dataset selection
- Reproducible Python environment using `uv`

---

## Project Structure
```
chaos-lab/
│
├── data/
│   └── raw/
│       └── usa-0025-p-r.txt
│
├── src/
│   └── chaos_lab/
│       ├── config/
│       ├── data/
│       ├── visualization/
│       └── main.py
│
└── pyproject.toml
```
---
## Installation
Clone the repository:
```bash
git clone https://github.com/avtomatik/chaos-lab.git
cd chaos-lab
```
Install dependencies:
```bash
uv sync
```
---
## Usage
Run with the default dataset:
```bash
uv run python -m chaos_lab.main
```
Use a custom dataset:
```bash
uv run python -m chaos_lab.main \
    --dataset data/raw/my_dataset.txt
```
---
## Example
The current implementation generates a cobweb diagram from a discrete trajectory:
```
input dataset
      |
      v
time-series normalization
      |
      v
trajectory transformation
      |
      v
cobweb coordinates
      |
      v
visualization
```
---
## Technologies
- Python 3
- pandas
- numpy
- matplotlib
- uv
---
## Roadmap
Possible future experiments:
- Logistic map simulation
- Bifurcation diagrams
- Lyapunov exponent calculation
- Strange attractor visualization
- Numerical experiments with chaotic systems
- Alternative computational backends (Rust / C++)
---
## References
- [Cobweb plot](https://en.wikipedia.org/wiki/Cobweb_plot)
- [Chaos theory](https://en.wikipedia.org/wiki/Chaos_theory)
---
## License
[MIT License](LICENSE.md)
