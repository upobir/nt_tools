import unittest
from nt_tools.primes import *

# TODO memoize brute tests

class TestPrimes(unittest.TestCase):
    def setUp(self) ->None:
        __doc__
        pass

    def tearDown(self) -> None:
        __doc__
        pass

    def brute_is_prime(self, x: int) -> bool:
        """checks if x is prime via brute force"""
        if x < 2:
            return False

        for i in range(2, x):
            if x % i == 0:
                return False
        return True

    def test_is_prime(self) -> None:
        """tests is_prime"""
        for i in range(1, 1001):
            self.assertEqual(self.brute_is_prime(i), is_prime(i))

        with self.assertRaises(Exception):
            is_prime(0)

        with self.assertRaises(Exception):
            is_prime(-1)


    def test_primes_in_range(self) -> None:
        """tests primes_in_range"""
        for l in range(-10, 100+1):
            for r in range(-10, 100+1):
                i = l
                primes = []
                while i < r:
                    if self.brute_is_prime(i):
                        primes.append(i)
                    i += 1

                self.assertEqual(primes, primes_in_range(l, r))

    def test_random_prime_in_range(self) -> None:
        """tests random_prime_in_range"""
        for l in range(-10, 100+1):
            for r in range(-10, 100+1):
                x = random_prime_in_range(l, r)

                if x is None:
                    i = l
                    while i < r:
                        self.assertFalse(self.brute_is_prime(i), f"{l}, {r}")
                        i += 1
                else:
                    self.assertTrue(x < r)
                    self.assertTrue(l <= x)

                    self.assertTrue(self.brute_is_prime(x))

        for i in range(10):
            random_prime_in_range(1, 10, i)

        with self.assertRaises(Exception):
            random_prime_in_range(1, 10, -1)
