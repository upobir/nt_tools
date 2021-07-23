from typing import Tuple, Optional
from math import lcm
# import nt_tools.mod_integer as m
from nt_tools.mod_integer import *

def bezout(a: int, b: int) -> Tuple[int, int, int]:
    """extended euclidean algorithm is performed and x, y, g are returned so that a*x+b*y = g"""
    if b == 0:
        return 1, 0, a
    
    g: int; x: int; y: int
    x, y, g = bezout(b, a % b)

    return y, x-y*(a//b), g



def crt(*args: "ModInteger") -> Optional["ModInteger"]:
    if len(args) == 0 :
        raise Exception("no argument provided")

    from nt_tools.mod_integer import ModInteger

    result: ModInteger = args[0]

    for i in range(1, len(args)):
        x: ModInteger = args[i]
    
        p, _, g = bezout(x.mod, result.mod)
        if (result.value-x.value) % g != 0:
            return None
        
        value: int = ((result.value-x.value) // g) * p * x.mod + x.value

        mod: int = lcm(result.mod, x.mod)

        result = ModInteger(value, mod)

    return result

