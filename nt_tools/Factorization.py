from typing import Optional
from random import randint
from nt_tools.ModInteger import *

def is_prime(x: int, iterations: Optional[int] = None) -> bool:
    """rabin miller algorithm to test primality of a number"""
    if x <= 0:
        raise Exception("'{}' is non-positive".format(x))
        
    if iterations is None:
        iterations = max(15, x.bit_length())

    if x < 4:
        return x != 1
    
    if x % 2 == 0:
        return x == 2

    e: int = 0
    y: int = x-1
    while(y % 2 == 0):
        y //= 2
        e += 1

    for _ in range(iterations):
        witness:int = randint(2, x-2)
        witness = (M(witness, x) ** y).value
        if witness <= 1:
            continue

        for _ in range(e):
            if(witness == x-1):
                break
            witness = (witness * witness) % x
            
        if witness != x-1:
            return False

    return True
