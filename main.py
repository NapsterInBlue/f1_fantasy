from src.ingest_data import load_constructor_ranks, load_driver_ranks, load_pick_orders
from src.common import Degenerate, ConstructorRank, DriverRank, PickOrder, DEGENERATES
from src.snake_draft import run_snake_draft


class DiamondDogs:
    def __init__(self):
        constructor_ranks = load_constructor_ranks()
        driver_ranks = load_driver_ranks()
        pick_orders = load_pick_orders()

        self.race_week = {
            name: Degenerate(
                name, pick_orders[name], driver_ranks[name], constructor_ranks[name]
            )
            for name in DEGENERATES
        }

    def pick_order(self, driver_mode: bool):
        if driver_mode:
            driver_orders = {
                name: self.race_week[name].pick_order["Driver"]
                for name in self.race_week
            }

            pick_order = [
                x[0] for x in sorted(driver_orders.items(), key=lambda item: item[1])
            ]

        else:
            constructor_orders = {
                name: self.race_week[name].pick_order["Constructor"]
                for name in self.race_week
            }

            pick_order = [
                x[0]
                for x in sorted(constructor_orders.items(), key=lambda item: item[1])
            ]

        return pick_order


if __name__ == "__main__":
    dd = DiamondDogs()
    print(dd.race_week)
    print(dd.pick_order(driver_mode=True))
    print(dd.pick_order(driver_mode=False))

    run_snake_draft(dd, driver_mode=True)