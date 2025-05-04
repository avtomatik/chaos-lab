#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May  4 12:23:47 2025

@author: alexandermikhailov
"""


import pandas as pd

from config import DATA_DIR, FILE_NAME
from transform import preprocess


def make_dataset() -> pd.DataFrame:
    file_path = DATA_DIR.joinpath(FILE_NAME)
    return pd.read_csv(file_path, index_col=0).pipe(preprocess)
