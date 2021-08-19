from nt_tools.mod_integer import ModInteger
from nt_tools.arithmetic_functions import phi
from nt_tools.factorization import factorize_exponent
from math import gcd

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