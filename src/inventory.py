class Inventory:
    def __init__(self, items: dict[str, int]):
        # Initializes the inventory with a dictionary of items and their quantities
        self.items = items

    def add(self, name: str, qty: int):
        # Adds a new item or increases the quantity of an existing item
        if name in self.items:
            self.items[name] += qty
        else:
            self.items[name] = qty

    def delete(self, name: str):
        # Deletes an item from the inventory
        if name in self.items:
            del self.items[name]

    def increase(self, name: str, qty: int):
        # Increases the quantity of an existing item
        if name in self.items:
            self.items[name] += qty
            print(f"Increased {qty} of {name}. New quantity: {self.items[name]}")

    def decrease(self, name: str, qty: int):
        # Decreases the quantity of an item if there's enough stock
        if name in self.items:
            if self.items[name] >= qty:
                self.items[name] -= qty
                print(f"Decreased {qty} of {name}. New quantity: {self.items[name]}")

    def view(self):
        # Displays the current inventory
        if not self.items:
            print("The inventory is empty.")
        else:
            print("Current inventory:")
            for name, qty in self.items.items():
                print(f"{name}: {qty}")
