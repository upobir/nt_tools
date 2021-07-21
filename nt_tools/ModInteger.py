from typing import Optional, Union

# TODO make immutable?

class ModInteger:
    """Mod Integer class that holds value and a mod"""

    default_mod: Optional[int] = None

    def __init__(self, value: int = 0, mod: Optional[int] = None) -> None:
        """Constructor to create ModInteger using value with mod, mod is defaulted to default_mod"""
        if mod is None:
            if ModInteger.default_mod is None:
                raise Exception("default mod is not set and no mod provided")
            else:
                mod = ModInteger.default_mod

        if mod <= 0:
            raise Exception("Invalid Mod '{}'".format(mod))

        self.value: int = value % mod
        self.mod: int = mod

    def __repr__(self) -> str:
        """representation operator for python repl"""
        return '< ' + str(self.value) + ' (mod '+str(self.mod)+')>'

    def __str__(self) -> str:
        """string operator to print value"""
        return str(self.value)

    def __add__(self, m: Union[int, "ModInteger"]) -> "ModInteger":
        """addition operator, integer of ModInteger can be added"""
        if isinstance(m, int):
            m = ModInteger(m, self.mod)
        if self.mod != m.mod:
            raise Exception("mods '{}' and '{}' do not match".format(self.mod, m.mod))
        return ModInteger(self.value+m.value, self.mod)

    def __sub__(self, m: Union[int, "ModInteger"]) -> "ModInteger":
        """subtraction operator, integer of ModInteger can be added"""
        if isinstance(m, int):
            m = ModInteger(m, self.mod)
        if self.mod != m.mod:
            raise Exception("mods '{}' and '{}' do not match".format(self.mod, m.mod))
        return ModInteger(self.value-m.value, self.mod)

    def __mul__(self, m: Union[int, "ModInteger"]) -> "ModInteger":
        """multiplication operator, integer of ModInteger can be added"""
        if isinstance(m, int):
            m = ModInteger(m, self.mod)
        if self.mod != m.mod:
            raise Exception("mods '{}' and '{}' do not match".format(self.mod, m.mod))
        return ModInteger(self.value*m.value, self.mod)

M = ModInteger