#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 11 22:17:06 2022

@author: Alexander Mikhailov
"""


import numpy as np

from dataset import make_dataset
from plots import make_plot


def main() -> None:
    """
    Draws cobweb plot or Verhulst diagram for Given Dataset

    Returns
    -------
    None
        DESCRIPTION.

    """
    df = make_dataset()

    last_column = df.iloc[:, [-1]]
    x_lin = np.linspace(last_column.min(), last_column.max(), 100)

    df.pipe(make_plot, x_lin)


if __name__ == '__main__':
    main()
