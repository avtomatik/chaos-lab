from pathlib import Path

import pandas as pd


def read_dataset(dataset_path: Path) -> pd.DataFrame:
    return pd.read_csv(dataset_path, index_col=0)
