from typing import Optional, Union
from math import gcd
from nt_tools.diophantine import diophantine

# TODO make immutable?
# TODO floor divide?

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

    def __eq__(self, o: object) -> bool:
        """equality operator for two mod integers"""
        if isinstance(o, ModInteger):
            return self.value == o.value and self.mod == o.mod
        return NotImplemented

    def __add__(self, m: Union[int, "ModInteger"]) -> "ModInteger":
        """addition operator, integer of ModInteger can be added"""
        if isinstance(m, int):
            m = ModInteger(m, self.mod)
        if self.mod != m.mod:
            raise Exception("mods '{}' and '{}' do not match".format(self.mod, m.mod))
        return ModInteger(self.value+m.value, self.mod)

    def __sub__(self, m: Union[int, "ModInteger"]) -> "ModInteger":
        """subtraction operator, integer of ModInteger can be subtracted"""
        if isinstance(m, int):
            m = ModInteger(m, self.mod)
        if self.mod != m.mod:
            raise Exception("mods '{}' and '{}' do not match".format(self.mod, m.mod))
        return ModInteger(self.value-m.value, self.mod)

    def __mul__(self, m: Union[int, "ModInteger"]) -> "ModInteger":
        """multiplication operator, integer of ModInteger can be multiplied"""
        if isinstance(m, int):
            m = ModInteger(m, self.mod)
        if self.mod != m.mod:
            raise Exception("mods '{}' and '{}' do not match".format(self.mod, m.mod))
        return ModInteger(self.value*m.value, self.mod)

    def is_invertible(self) -> bool:
        """function to check if mod integer is invertible in current mod"""
        return gcd(self.value, self.mod) == 1

    def inverse(self) -> "ModInteger":
        """get inverse for mod integer"""
        x, _, g = diophantine(self.value, self.mod)
        if g != 1:
            raise Exception("'{}' is not invertible w.r.t. mod '{}'".format(self.value, self.mod))
        
        return ModInteger(x, self.mod)

    def __truediv__(self, m: Union[int, "ModInteger"]) -> "ModInteger":
        """division operator, integer of ModInteger can be divided"""
        if isinstance(m, int):
            m = ModInteger(m, self.mod)
        if self.mod != m.mod:
            raise Exception("mods '{}' and '{}' do not match".format(self.mod, m.mod))

        return self * m.inverse()

    def __pow__(self, exponent: int) -> "ModInteger":
        """Integer Exponentiation"""
        if exponent == 0:
            return ModInteger(1, self.mod)
        elif exponent > 0:
            result: "ModInteger" = (self*self) ** (exponent // 2)
            if exponent % 2 == 1:
                result = result * self
            return result
        else:
            return self.inverse() ** (-exponent)

M = ModInteger