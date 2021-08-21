import nt_tools

# mod_integer
print("mod_integer")

nt_tools.M.default_mod = 10**9+7
x = nt_tools.M(1)
y = nt_tools.M(2)
z = x+y

print(x)
print(y)
print(x+y)
print(x-y)
print(x*y)
print(x/y)
print(y**2)
print(y**-1)

print(nt_tools.guess_int_from_modint(nt_tools.M(10, 100)))
print(nt_tools.guess_int_from_modint(nt_tools.M(-10, 100)))

print()

# factorization
print("factorization")

print(nt_tools.factorize(10**18-10))
print(nt_tools.factorize_exponent(10**18-10))
print(nt_tools.p_adic(100, 5))
print(nt_tools.divisors(100))

print()


# arithmetic_functions
print("arithmetic_functions")

print(nt_tools.tau(60))
print(nt_tools.sigma(60))
print(nt_tools.mu(30))
print(nt_tools.phi(60))
print(nt_tools.Omega(60))
print(nt_tools.omega(60))

print()

# diophantine
print("diophantine")

a = 10
b = 14
x, y, g = nt_tools.bezout(a, b)
print("{}({}) + {}({}) = {}".format(a, x, b, y, g))

c = 50
x, y = nt_tools.diophantine(a, b, c)
print("{}({}) + {}({}) = {}".format(a, x, b, y, c))
print(nt_tools.lcm(a, b))
print(repr(nt_tools.crt(nt_tools.M(1, 7), nt_tools.M(2, 5))))

print()

# primes
print("primes")

print(nt_tools.primes_in_range(10, 26))
print(nt_tools.random_prime_in_range(10**9, 10**9+50))
print(nt_tools.is_prime(10**18-11))

print()

# exponentiation
print("exponentiation")

print(nt_tools.order(nt_tools.M(5, 96)))
print(nt_tools.is_quadratic_residue(nt_tools.M(-1, 10)))
print(nt_tools.has_primitive_root(50))

print()