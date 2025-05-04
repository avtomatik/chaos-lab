#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May  4 13:06:41 2025

@author: alexandermikhailov
"""


import pandas as pd


def preprocess(df: pd.DataFrame) -> pd.DataFrame:
    """
    Preprocesses the dataset by normalizing it and generating a transformed
    DataFrame.

    Parameters
    ----------
    df : pd.DataFrame
        Input DataFrame to be preprocessed.

    Returns
    -------
    pd.DataFrame
        A DataFrame with calculated values and their shifted versions.
    """
    df_normalized = df.div(df.iloc[0, :])

    calc_values = []
    for _, row in df_normalized.iterrows():
        value = row.iloc[0]
        calc_values.extend([value, value])

    calc_values = calc_values[1:]

    calculated = pd.DataFrame({'calculated': calc_values})

    result = pd.concat([calculated, calculated.shift(-1)], axis=1).dropna()

    return result
