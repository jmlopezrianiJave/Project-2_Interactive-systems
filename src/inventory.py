class inventory:
    def __init__(self,
        items: dict[str, int]
    ):
        self.items = items

    def add(self, name: str, qty: int):
        
