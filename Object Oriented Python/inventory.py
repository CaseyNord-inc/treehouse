# Super! Code Challenge


class Inventory:
    def __init__(self):
        self.slots = []

    def add_item(self, item):
        self.slots.append(item)


class SortedInventory(Inventory):
    def add_item(self, item):
        super().add_item(item)
        self.slots.sort()
