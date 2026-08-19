import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


def plot_cobweb_diagram(df: pd.DataFrame, param_line: np.ndarray) -> None:
    """
    Generate a cobweb plot.
    Parameters
    ----------
    df:
        Dataframe containing Y_t and Y_t_plus_1 coordinates.
    param_line:
        Values for identity function Y_t = Y_(t+1).
    """
    plt.figure(figsize=(8, 6))
    plt.plot(df["Y_t"], df["Y_t_plus_1"], label="Trajectory", linewidth=0.8)
    plt.plot(param_line, param_line, label="$Y_t = Y_{t+1}$", linewidth=0.8)
    plt.xlabel("$Y_t$")
    plt.ylabel("$Y_{t+1}$")
    plt.title("Cobweb Plot")
    plt.grid(True)
    plt.legend()
    plt.tight_layout()
    plt.show()
