from typing import List, Optional
from math import sqrt, ceil, log
from random import randint
from nt_tools.factorization import is_prime

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