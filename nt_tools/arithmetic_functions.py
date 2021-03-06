from nt_tools.factorization import factorize, factorize_exponent

def count_of_prime_factors(n: int) -> int:
    """return count of prime factor (possible duplicate) of n"""
    if(n <= 0):
        raise Exception(f"'{n}' is non-positive")

    return len(factorize(n))

Omega = count_of_prime_factors

def count_of_distinct_prime_factors(n: int) -> int:
    """return count of distinct prime factor of n"""
    if(n <= 0):
        raise Exception(f"'{n}' is non-positive")

    return len(factorize_exponent(n))

omega = count_of_distinct_prime_factors

def count_of_divisors(n: int) -> int:
    """returns count of divisors of n"""
    if(n <= 0):
        raise Exception(f"'{n}' is non-positive")

    factorization = factorize_exponent(n)

    result: int = 1
    for _, exponent in factorization:
        result *= exponent+1

    return result

tau = count_of_divisors

def sum_of_divisors(n: int) -> int:
    """return sum of divisors of n"""
    if(n <= 0):
        raise Exception(f"'{n}' is non-positive")

    factorization = factorize_exponent(n)

    result: int = 1
    for prime, exponent in factorization:
        result *= (prime**(exponent+1)-1)//(prime-1)

    return result

sigma = sum_of_divisors

def mobius(n: int) -> int:
    """returns the mobius function value of a number"""
    if(n <= 0):
        raise Exception(f"'{n}' is non-positive")

    factorization = factorize_exponent(n)

    result: int = 1
    for _, exponent in factorization:
        if exponent > 1:
            return 0
        result = -result

    return result

mu = mobius

def totient(n: int) -> int:
    """returns the euler's totient function value of a number"""
    if(n <= 0):
        raise Exception(f"'{n}' is non-positive")

    factorization = factorize_exponent(n)

    result: int = n
    for prime, _ in factorization:
        result -= result // prime

    return result

phi = totient