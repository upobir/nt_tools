import unittest
from nt_tools.primes import *

class TestPrimes(unittest.TestCase):
    def setUp(self) ->None:
        __doc__
        pass

    def tearDown(self) -> None:
        __doc__
        pass

    def brute_is_prime(self, x: int) -> bool:
        if x < 2:
            return False

        for i in range(2, x):
            if x % i == 0:
                return False
        return True

    def test_is_prime(self) -> None:
        for i in range(1, 1001):
            self.assertEqual(self.brute_is_prime(i), is_prime(i))

        with self.assertRaises(Exception):
            is_prime(0)

        with self.assertRaises(Exception):
            is_prime(-1)


    def test_primes_in_range(self) -> None:
        for l in range(-100, 100+1):
            for r in range(-100, 100+1):
                i = l
                primes = []
                while i < r:
                    if self.brute_is_prime(i):
                        primes.append(i)
                    i += 1

                self.assertEqual(primes, primes_in_range(l, r))