from nt_tools.mod_integer import ModInteger, M
from nt_tools.arithmetic_functions import phi
from nt_tools.factorization import factorize_exponent
from typing import Optional, Dict, List
from math import exp, gcd
from random import randint

def order(x: ModInteger, candidate: Optional[int] = None) -> int:
    """computes multiplicative order of mod intger (x, mod), optionally a candidate can be provided such that x ** candidate = 1 modulo mod"""
    if gcd(x.value, x.mod) > 1:
        raise Exception(f"'{x.value}' is not coprime to '{x.mod}'")

    if candidate is None:
        candidate = phi(x.mod)
    elif (x ** candidate).value != 1:
        raise Exception(f"'{x.value}^{candidate} mod {x.mod}' is not 1")

    ret: int = candidate

    for prime, exponent in factorize_exponent(candidate):
        for _ in range(exponent):
            if (x ** (ret//prime)).value == 1:
                ret //= prime
            else:
                break

    return ret

def is_quadratic_residue(x: ModInteger) -> bool:
    """checks whether x is a quadratic residue modulo it's mod"""
    mod: int = x.mod

    for prime, exponent in factorize_exponent(mod):
        if prime == 2:
            if not _is_quadratic_residue_mod_power_of_two(x.value, exponent):
                return False
        else:
            if not _is_quadratic_residue_mod_power_of_odd_prime(x.value, prime, exponent):
                return False

    return True

def _is_quadratic_residue_mod_power_of_two(value: int, exponent: int) -> bool:
    """internal method to test quadratic residue modulo 2^exponent"""
    value %= (2 ** exponent)

    if value == 0:
        return True

    while value > 1 and value % 4 == 0:
        value //= 4

    return (value % 8 == 1)

def _is_quadratic_residue_mod_power_of_odd_prime(value: int, prime: int, exponent: int) -> bool:
    """internal method to test quadratice residue module prime^exponent"""
    if prime % 2 == 0:
        raise Exception(f"'{prime}' is not odd")

    value %= (prime ** exponent)

    if value == 0:
        return True

    prime_square: int = prime * prime
    while value > 1 and value % prime_square == 0:
        value //= prime_square

    return (M(value, prime) ** ((prime-1)//2)).value == 1

def has_primitive_root(mod: int) -> bool:
    """cheks if there is a primitive modulo mod"""
    if mod == 1:
        return False
    elif mod == 2 or mod == 4:
        return True

    if mod % 2 == 0:
        mod //= 2

    if mod % 2 == 0:
        return False

    return len(factorize_exponent(mod)) == 1

def get_smallest_primitive_root(mod: int) -> Optional[int]:
    """returns smallest primitive root modulo mod, or none if there aren't any"""

    if not has_primitive_root(mod):
        return None

    candidate: ModInteger = M(1, mod)
    phi_val: int = phi(mod)
    while True:
        if _is_primitive_root(candidate, phi_val):
            return candidate.value
        candidate.value += 1


def get_random_primitive_root(mod: int) -> Optional[int]:
    """returns a random primitive root modulo mod, or none if there aren't any"""

    if not has_primitive_root(mod):
        return None

    swapped: Dict[int, int] = {}
    phi_val: int = phi(mod)
    while True:
        candidate_index: int = randint(1, mod-1)
        candidate: int = swapped.get(candidate_index, candidate_index)
        if _is_primitive_root(M(candidate, mod), phi_val):
            return candidate

def _is_primitive_root(x: ModInteger, phi_value: Optional[int] = None) -> bool:
    """internal functiont test if x is primitive root modulo mod"""

    if gcd(x.value, x.mod) != 1:
        return False
    return order(x, phi_value) == phi_value

def get_all_primitive_roots(mod: int) -> List[int]:
    """returns list of all primitive roots of a mod"""

    root: Optional[int] = get_random_primitive_root(mod)

    if root is None:
        return list()
    
    root_m: ModInteger = M(root, mod)
    phi_value: int = phi(mod)

    roots: List[int] = [root_m.value]

    for i in range(2, phi_value):
        root_m *= root

        if gcd(i, phi_value) == 1:
            roots.append(root_m.value)

    return sorted(roots)
