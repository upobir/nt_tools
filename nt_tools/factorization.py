from typing import Callable, Optional, List, Tuple
from random import randint
from math import gcd
from nt_tools.primes import is_prime


def p_adic(x: int, p: int) -> int:
    """function that returns the p-adic value of x, i.e. maximum exponent of p that divides x"""
    if x == 0:
        raise Exception(f"x == 0")
    if abs(p) < 2:
        raise Exception(f"'abs({p})' is less than 1")

    exponent: int = 0
    while x % p == 0:
        x //= p
        exponent += 1
    
    return exponent

def pollard_rho(n: int) -> int:
    """function to return a divisor of composite n, if n is prime, it will fall in infinite loop"""
    if n <= 0:
        raise Exception(f"'{n}' is non-positive")

    if n <= 3:
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

def divisors(n: int) -> List[int]:
    """function that returns a sorted list of divisors fo n"""
    if n <= 0:
        raise Exception(f"'{n}' is non positive")

    factors: List[Tuple[int, int]] = factorize_exponent(n)

    result: List[int] = _divisor_generator(factors).generate()

    result.sort()

    return result

class _divisor_generator:
    """intenal class that takes a list of (prime, exponent) and generates all divisors"""
    def __init__(self, factors: List[Tuple[int, int]]) -> None:
        self.factors: List[Tuple[int, int]] = factors

    def generate(self) -> List[int]:
        self.result: List[int] = []

        self.recursive_generate()

        self.result.sort()
        return self.result

    def recursive_generate(self, pos: int = 0, divisor: int = 1) -> None:
        if(pos == len(self.factors)):
            self.result.append(divisor)
            return

        prime, exponent = self.factors[pos]

        for _ in range(exponent+1):
            self.recursive_generate(pos+1, divisor)
            divisor *= prime