from typing import Dict, List, Tuple
from pathlib import Path

HERE = Path(__file__).resolve()
DATA = str(HERE.parent.parent)

import pandas as pd

from src.common import ConstructorRank, DriverRank, PickOrder
from src.common import DEGENERATES


def load_pick_orders():
    df = pd.read_csv(DATA + "/pick_order.csv", index_col=0)

    assert sorted(df.loc["Driver"].values) == list(range(1, len(DEGENERATES) + 1))
    assert sorted(df.loc["Constructor"].values) == list(range(1, len(DEGENERATES) + 1))

    return df.to_dict()


def load_driver_ranks() -> Dict[str, List[Tuple[int, str]]]:
    df = pd.read_csv(DATA + "/driver_ranks.csv")

    return df.to_dict()


def load_constructor_ranks() -> Dict[str, List[Tuple[int, str]]]:
    df = pd.read_csv(DATA + "/constructor_ranks.csv")

    return df.to_dict()


if __name__ == "__main__":
    print(load_pick_orders())
    print(load_driver_ranks())
    print(load_constructor_ranks())