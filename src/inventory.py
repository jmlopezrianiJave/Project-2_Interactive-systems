class Inventory:
    def __init__(self, equipment: dict[str, int]):
        self.equipment = equipment

    def add(self, name: str, qty: int):
        if name in self.equipment:
            self.equipment[name] += qty
        else:
            self.equipment[name] = qty

    def delete(self, name: str):
        if name in self.equipment:
            del self.equipment[name]

    def increase(self, name: str, qty: int):
        if name in self.equipment:
            self.equipment[name] += qty
            print(f"Increased {qty} of {name}. New quantity: {self.equipment[name]}")

    def decrease(self, name: str, qty: int):
        if name in self.equipment:
            if self.equipment[name] >= qty:
                self.equipment[name] -= qty
                print(f"Decreased {qty} of {name}. New quantity: {self.equipment[name]}")

    def view(self):
        if not self.equipment:
            print("The inventory is empty.")
        else:
            print("Current inventory:")
            for name, qty in self.equipment.items():
                print(f"{name}: {qty}")
