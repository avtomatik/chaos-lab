import argparse
from pathlib import Path

import numpy as np

from chaos_lab.config.paths import RAW_DATA_DIR
from chaos_lab.data.reader import read_dataset
from chaos_lab.data.transform import build_cobweb_points
from chaos_lab.visualization.plot import plot_cobweb_diagram

DEFAULT_DATASET = RAW_DATA_DIR / "usa-0025-p-r.txt"


def parse_arguments() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Generate a cobweb plot from a time series dataset."
    )
    parser.add_argument(
        "--dataset",
        type=Path,
        default=DEFAULT_DATASET,
        help="Path to input dataset.",
    )
    return parser.parse_args()


def run(dataset_path: Path) -> None:
    raw_dataset = read_dataset(dataset_path)
    cobweb_points = build_cobweb_points(raw_dataset)
    values = cobweb_points["Y_t_plus_1"]
    identity_line = np.linspace(values.min(), values.max(), 100)
    plot_cobweb_diagram(cobweb_points, identity_line)


def main() -> None:
    args = parse_arguments()
    run(args.dataset)


if __name__ == "__main__":
    main()
