from typing import List
from math import sqrt, ceil

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

        start: int = max(3, (L+p-1)//p) * p
        if start % 2 == 0:
            start += p

        for m in range(start, R, p+p):
            marked2[m-L] = True

    start: int = L if L % 2 == 1 else L+1

    result: List[int] = [x for x in range(start, R, 2) if not marked2[x-L]]
    if L <= 2 < R:
        result = [2] + result

    return result