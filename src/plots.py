#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May  4 13:12:57 2025

@author: alexandermikhailov
"""


import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


def make_plot(df: pd.DataFrame, param_line: np.ndarray) -> None:
    """
    Generates a cobweb plot from the given dataset.

    Parameters
    ----------
    df : pd.DataFrame
        A DataFrame where the first column is interpreted as Y_t and the
        second as Y_{1+t}.
    param_line : np.ndarray
        An array used to plot the identity line Y_t = Y_{1+t}.

    Returns
    -------
    None
    """
    plt.figure(figsize=(8, 6))

    plt.plot(
        df.iloc[:, 0],
        df.iloc[:, 1],
        label='Series',
        linewidth=0.5
    )

    plt.plot(
        param_line,
        param_line,
        label='$Y_t = Y_{1+t}$',
        color='black',
        linewidth=0.5
    )

    plt.xlabel('$Y_t$')
    plt.ylabel('$Y_{1+t}$')
    plt.title('Cobweb Plot')
    plt.grid(True)
    plt.legend()
    plt.tight_layout()
    plt.show()
