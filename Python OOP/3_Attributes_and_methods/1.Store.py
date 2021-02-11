from _collections import defaultdict

class Store:
    def __init__(self, name, type, capacity):
        self.name = name
        self.type = type
        self.capacity = capacity
        self.items = defaultdict(int)

    @classmethod
    def from_size(cls, name, type, size):
        return cls(name, type, int(size/2))

    def add_item(self, item_name):
        if sum(self.items.values()) + 1 <= self.capacity:
            self.items[item_name] += 1
            return f'{item_name} added to the store'
        return 'Not enough capacity in the store'

    def remove_item(self, item_name, amount):
        if self.items[item_name] >= amount:
            self.items[item_name] -= amount
            return f"{amount} {item_name} removed from the store"
        return f'Cannot remove {amount} {item_name}'

    def __repr__(self):
        return f"{self.name} of type {self.type} with capacity {self.capacity}"
