from typing import Dict

from src.common import CONSTRUCTORS, DRIVERS, Degenerate


AVAILABLE_DRIVERS = set(DRIVERS)
AVAILABLE_CONSTRUCTORS = set(CONSTRUCTORS)


def run_driver_snake_draft(degenerates: "DiamondDogs"):
    pick_order = degenerates.pick_order(driver_mode=True)
    reversed_pick_order = pick_order[::-1]

    full_draft = pick_order + reversed_pick_order

    print("--- Driver Draft ---")
    for pick in full_draft:
        driver = pick_next_available_driver(degenerates[pick])
        degenerates[pick].this_weeks_drivers.append(driver)
        print(f"{pick}:\t\t{driver}")


def pick_next_available_driver(degenerate: Degenerate) -> str:
    for (idx, driver) in degenerate.driver_rank.items():
        if driver in AVAILABLE_DRIVERS:
            AVAILABLE_DRIVERS.remove(driver)
            return driver


def run_constructor_snake_draft(degenerates: "DiamondDogs"):
    pick_order = degenerates.pick_order(driver_mode=False)
    full_draft = pick_order

    print("--- Constructor Draft ---")
    for pick in full_draft:
        constructor = pick_next_available_constructor(degenerates[pick])
        degenerates[pick].this_weeks_constructors.append(constructor)
        print(f"{pick}:\t\t{constructor}")


def pick_next_available_constructor(degenerate: Degenerate) -> str:
    for (idx, constructor) in degenerate.constructor_rank.items():
        if constructor in AVAILABLE_CONSTRUCTORS:
            AVAILABLE_CONSTRUCTORS.remove(constructor)
            return constructor