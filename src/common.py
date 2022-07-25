from typing import Dict, List

DEGENERATES = ["Ann", "Brigoe", "Jay", "Matt", "Vero", "Nick"]

DRIVERS = [
    "Lewis Hamilton",
    "George Russell",
    "Max Verstappen",
    "Sergio Perez",
    "Charles Leclerc",
    "Carlos Sainz",
    "Daniel Ricciardo",
    "Lando Norris",
    "Fernando Alonso",
    "Esteban Ocon",
    "Pierre Gasly",
    "Yuki Tsunoda",
    "Sebastian Vettel",
    "Lance Stroll",
    "Nicholas Latifi",
    "Alex Albon",
    "Valtteri Bottas",
    "Zhou Guanyu",
    "Kevin Magnussen",
    "Mick Schumacher",
]

CONSTRUCTORS = [
    "Mercedes",
    "Red Bull",
    "Ferrari",
    "McLaren",
    "Alpine",
    "AlphaTauri",
    "Aston Martin",
    "Williams",
    "Alfa Romeo",
    "Haas",
]


class DriverRank:
    def __init__(self, order_driver_dict: Dict[int, str]):
        self.order_driver_dict = order_driver_dict

        assert len(order_driver_dict.values()) == len(DRIVERS)
        assert (driver in DRIVERS for driver in order_driver_dict.values())
        assert (driver in order_driver_dict.values() for driver in DRIVERS)


class ConstructorRank:
    def __init__(self, order_constructor_dict: Dict[int, str]):
        self.order_constructor_dict = order_constructor_dict

        assert len(order_constructor_dict.values()) == len(CONSTRUCTORS)
        assert (
            constructor in CONSTRUCTORS
            for constructor in order_constructor_dict.values()
        )
        assert (
            constructor in order_constructor_dict.values()
            for constructor in CONSTRUCTORS
        )


class PickOrder:
    def __init__(self, pick_order_dict: Dict[str, int]):
        self.driver = pick_order_dict["Driver"]
        self.constructor = pick_order_dict["Constructor"]


class Degenerate:
    def __init__(
        self,
        name: str,
        pick_order_dict: Dict,
        driver_rank_dict: Dict,
        constructor_rank_dict: Dict,
    ):
        self.name = name
        self.pick_order = pick_order_dict
        self.driver_rank = driver_rank_dict
        self.constructor_rank = constructor_rank_dict

        self.this_weeks_drivers = []
        self.this_weeks_constructors = []

    def __str__(self):
        return (
            ("Constructors: " + " ".join(self.this_weeks_constructors).ljust(25))
            + "Drivers: "
            + ",   ".join(self.this_weeks_drivers)
        )

    def __repr__(self):
        return str(self)


if __name__ == "__main__":
    dr = DriverRank({i: driver for (i, driver) in zip(range(1, 21), DRIVERS)})
    print(dr.order_driver_dict)

    cr = ConstructorRank(
        {i: constructor for (i, constructor) in zip(range(1, 11), CONSTRUCTORS)}
    )
    print(cr.order_constructor_dict)