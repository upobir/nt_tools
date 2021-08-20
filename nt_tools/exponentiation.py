from nt_tools.mod_integer import ModInteger, M
from nt_tools.arithmetic_functions import phi
from nt_tools.factorization import factorize_exponent
from math import exp, gcd

def order(x: ModInteger) -> int:
    """computes multiplicative order of mod intger (x, mod) """
    if gcd(x.value, x.mod) > 1:
        raise Exception(f"'{x.value}' is not coprime to '{x.mod}'")

    phi_value: int = phi(x.mod)
    ret: int = phi_value

    for prime, exponent in factorize_exponent(phi_value):
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