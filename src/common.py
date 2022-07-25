from typing import List

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


class OrderedPreference:
    degenerate: str
    order: List[str]


class DriverRank:
    def __init__(self, degenerate: str, driver_order: List[str]):
        self.degenerate = degenerate
        self.order = driver_order

        assert len(driver_order) == len(DRIVERS)
        assert (driver in DRIVERS for driver in driver_order)
        assert (driver in driver_order for driver in DRIVERS)


class ConstructorRank:
    def __init__(self, degenerate: str, constructor_order: List[str]):
        self.degenerate = degenerate
        self.order = constructor_order

        assert len(constructor_order) == len(CONSTRUCTORS)
        assert (constructor in CONSTRUCTORS for constructor in constructor_order)
        assert (constructor in constructor_order for constructor in CONSTRUCTORS)


class PickOrder:
    def __init__(self, driver: int, constructor: int):
        self.driver = driver
        self.constructor = constructor


if __name__ == "__main__":
    dr = DriverRank("Nick", DRIVERS)
    print(dr.order)

    cr = ConstructorRank("Nick", CONSTRUCTORS)
    print(cr.order)