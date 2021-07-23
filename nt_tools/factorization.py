from typing import Callable, Optional, List, Tuple
from random import randint
from math import gcd
from nt_tools.mod_integer import *

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


def p_adic(x: int, p: int) -> int:
    """function that returns the p-adic value of x, i.e. maximum exponent of p that divides x"""
    exponent: int = 0
    while x % p == 0:
        x //= p
        exponent += 1
    
    return exponent

def pollard_rho(n: int) -> int:
    """function to return a divisor of n, unless n is prime or 1, the divisor should be proper"""
    if n <= 0:
        raise Exception(f"'{n}' is non-positive")

    if n < 3:
        return n

    if n % 2 == 0:
        return 2

    X: int = 2
    c: int = 1
    f: Callable[[int], int] = lambda input: (input*input + c) %n

    x: int = 0
    y: int = 0
    g: int = 1

    while g == 1:
        x = f(x)
        y = f(f(y))
        g = gcd(x-y, n)

        if x == y:
            c = randint(1, n-1)
            x = X
            y = f(X)
            g = 1

    return g

def factorize(n: int) -> List[int]:
    """function that factorizes x and returns a list of primes"""
    if n <= 0:
        raise Exception(f"'{n}' is non-positive")

    if n == 1:
        return []
    if is_prime(n):
        return [n]
    else:
        d: int = pollard_rho(n)
        return sorted(factorize(d) + factorize(n//d))

def factorize_exponent(n: int) -> List[Tuple[int, int]]:
    """function that factorizes x and returns a list of tuples (prime, exponent)"""
    if n <= 0:
        raise Exception(f"'{n}' is non-positive")

    primes_list: List[int] = factorize(n)

    result: List[Tuple[int, int]] = []

    prime: Optional[int] = None
    exponent: int = 0

    for x in primes_list:
        if prime == x:
            exponent += 1
        else:
            if prime is not None:
                result.append((prime, exponent))
            prime = x
            exponent = 1

    if prime is not None:
        result.append((prime, exponent))

    return result