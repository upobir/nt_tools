from typing import Tuple

def diophantine(a: int, b: int) -> Tuple[int, int, int]:
    """extended euclidean algorithm is performed and x, y, g are returned so that a*x+b*y = g"""
    if b == 0:
        return 1, 0, a
    
    g: int; x: int; y: int
    x, y, g = diophantine(b, a % b)

    return y, x-y*(a//b), g
