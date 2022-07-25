from typing import Dict

from src.common import CONSTRUCTORS, DRIVERS, Degenerate


AVAILABLE_DRIVERS = set(DRIVERS)
AVAILABLE_CONSTRUCTORS = set(CONSTRUCTORS)


def run_snake_draft(degenerates: "DiamondDogs", driver_mode: bool):
    pick_order = degenerates.pick_order(driver_mode=driver_mode)
    reversed_pick_order = pick_order[::-1]

    full_draft = pick_order + reversed_pick_order + pick_order

    for pick in full_draft:
        print(pick)


# def pick_next_driver(degenerate: Degenerate):
#     for
