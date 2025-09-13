from inventory import Inventory

class Choice:
    def __init__(self,
                 text: str,
                 target: int | None,
                 requiresInv: dict[str, int] = None,
                 requiresFlag: dict[str, bool] = None,
                 effectsInv: dict[str, int] = None,
                 effectsFlag: dict[str, bool] = None,
                 sound: str | None = None,
                 sound_pos: str | tuple[float, float, float] | None = None):
        self.text = text
        self.target = target
        self.requiresInv = requiresInv or {}
        self.requiresFlag = requiresFlag or {}
        self.effectsInv = effectsInv or {}
        self.effectsFlag = effectsFlag or {}
        self.sound = sound
        self.sound_pos = sound_pos or "center"

    def is_available(self,inv:Inventory, flags:dict[str,bool]) -> bool:
        for name, qty in self.requiresInv.items():
            if inv.equipment.get(name,0) < qty:
                return False
        for f, state in self.requiresFlag.items():
            cur = flags.get(f, False)
            if cur != state:
                return False
        return True

    def apply_effects(self,inv:Inventory, flags:dict[str,bool])->None:
        for item, qty in self.effectsInv.items():
            if qty < 0:
                rmv = -qty
                if item in inv.equipment:
                    if inv.equipment[item] > rmv:
                        inv.decrease(item, rmv)
                    else:
                        inv.delete(item)
            elif qty > 0:
                if item in inv.equipment:
                    inv.increase(item, qty)
                else:
                    inv.add(item, qty)
        for f, toggle in self.effectsFlag.items():
            flags[f] = bool(toggle)