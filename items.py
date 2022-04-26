from dataclasses import dataclass
from collections import OrderedDict


class Item:
    name: str = "item name"
    id: int
    qty: int
    description = "description"
    location: str = "location"
    handling: str = "Default"


pick1 = Item('Raspberry pi 7in. touch display', 1001,1, 
"A touch screen display for raspberry pi in a xbyx box", 
"Aisle 1, Slot 3")

pick2 = Item('Watch', 1002, 2, "Casio men's watch", "Aisle 2, slot 6")

pick3 = Item('Glass vase', 1006, 1, "glass vase brand etc", "Aisle 1, slot 2")

itemList = {'C-263':pick1, 'C-266':pick2, 'C-269':pick3}
