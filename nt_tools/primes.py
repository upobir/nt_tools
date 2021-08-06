from typing import List, Optional
from math import sqrt, ceil, log
from random import randint
from nt_tools.mod_integer import M

def is_prime(x: int, iterations: Optional[int] = None) -> bool:
    """rabin miller algorithm to test primality of a number"""
    if x <= 0:
        raise Exception(f"'{x}' is non-positive")
        
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

def primes_in_range(L: int, R: int) -> List[int]:
    """generates and returns list of prime in range [L, R)"""
    L = max(2, L)
    R = max(L, R)
    limit: int = int(ceil(sqrt(R))) + 1

    marked1: List[bool] = [False] * limit
    marked2: List[bool] = [False] * (R-L)

    for p in range(3, limit, 2):
        if marked1[p]:
            continue

        for m in range(p*p, limit, p):
            marked1[m] = True

        m_start: int = max(3, (L+p-1)//p) * p
        if m_start % 2 == 0:
            m_start += p

        for m in range(m_start, R, p+p):
            marked2[m-L] = True

    start: int = L if L % 2 == 1 else L+1

    result: List[int] = [x for x in range(start, R, 2) if not marked2[x-L]]
    if L <= 2 < R:
        result = [2] + result

    return result

def random_prime_in_range(L: int, R: int, max_iter: Optional[int] = None) -> Optional[int]:
    """generates a random in range [L, R), returns None if max_iter iterations pass but no prime is found"""
    L = max(L, 1)
    if L >= R:
        return None

    if max_iter is None:
        max_iter = int(log(R)*10)


    for _ in range(max_iter):
        candidate: int = randint(L, R-1)
        if is_prime(candidate):
            return candidate
    
    return None