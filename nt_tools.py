from typing import Optional

DEFAULT_MOD: Optional[int] = None

class ModInteger:
    """Mod Integer class that holds value and a mod"""
    def __init__(self, value: int = 0, mod: Optional[int] = DEFAULT_MOD) -> None:
        if mod is None or mod <= 0:
            raise Exception("Invalid Mod '{}'".format(mod))

        self.value: int = value
        self.mod: int = mod

M = ModInteger