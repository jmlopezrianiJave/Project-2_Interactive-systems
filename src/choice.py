class Choice:
    def __init__(
                 text: str,
                 target: int,
                 requiresInv: dict[str, int] = None,
                 requiresFlag: list[str] = None,
                 effects: dict[str, int] = None):
        self.text = text
        self.target = target
        self.requiresInv = requiresInv or {}
        self.requiresFlag = requiresFlag or {}
        self.effects = effects or {}

    def is_available(self, game) -> bool:
        for r in self.requiresInv:
            for item in requiresInv:
                if game.inventory.items[item[0]] < item[1]:
                    return False
            for f in requiresFlag:
                if not(game.flags[f]):
                    return False
            return True