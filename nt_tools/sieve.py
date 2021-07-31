from typing import List
from math import sqrt, ceil

def primes_till(N: int) -> List[int]:
    marked = [False] * (N+1)

    limit: int = ceil(sqrt(N))+1
    for p in range(3, limit, 2):
        if marked[p]:
            continue

        for m in range(p*p, N+1, p):
            marked[m] = True


    result = [2] + [x for x in range(3, N+1, 2) if not marked[x]]
    return result