from typing import Optional

class ModInteger:
    """Mod Integer class that holds value and a mod"""

    default_mod: Optional[int] = None

    def __init__(self, value: int = 0, mod: Optional[int] = None) -> None:
        if mod is None:
            if ModInteger.default_mod is None:
                raise Exception("default mod is not set and no mod provided")
            else:
                mod = ModInteger.default_mod

        if mod <= 0:
            raise Exception("Invalid Mod '{}'".format(mod))

        self.value: int = value % mod
        self.mod: int = mod

M = ModInteger