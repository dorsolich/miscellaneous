from dataclass_decorator.dataclass import InventoryTracker
from dataclass_decorator.dataclass_decorator import InventoryItem


names = ["book", "pen"]
prices = [5, 2.5]
units = [2, 1]

def generate_inventory(Object, names, prices, units):
    items = {}
    for i, (name, price, unit) in enumerate(zip(names, prices, units)):
        model = Object(name, price, unit)
        totalcost = model.total_cost()
        item = model.__dict__
        item["total_cost"] = totalcost
        items[i] = item
    return items

def test_answer():
    with_decorator = generate_inventory(InventoryItem, names, prices, units)
    without_decorator = generate_inventory(InventoryTracker, names, prices, units)
    assert with_decorator == without_decorator