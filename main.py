from src.ingest_data import load_constructor_ranks, load_driver_ranks, load_pick_orders
from src.common import Degenerate, ConstructorRank, DriverRank, PickOrder, DEGENERATES


constructor_ranks = load_constructor_ranks()
driver_ranks = load_driver_ranks()
pick_orders = load_pick_orders()


race_week = {
    name: Degenerate(
        name, pick_orders[name], driver_ranks[name], constructor_ranks[name]
    )
    for name in DEGENERATES
}