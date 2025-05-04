#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May  4 12:06:21 2025

@author: alexandermikhailov
"""


from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

DATA_DIR = BASE_DIR.joinpath('data')

FILE_NAME = 'dataset_usa_0025_p_r.txt'
