import unittest
from functools import reduce
from operator import mul
from nt_tools.factorization import *

class TestFactorization(unittest.TestCase):
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

    def test_p_adic(self) -> None:
        """test p_adic function"""

        data = [
            (100, 5, 2),
            (200, 10, 2),
            (500, 500, 1),
            (81, 4, 0),
            (245, 7, 2),
            (-245, 7, 2),
            (245, -7, 2),
            (-245, -7, 2)
        ]

        for x, p, e in data:
            self.assertEqual(p_adic(x, p), e)

        exception_data = [
            (100, 1),
            (100, -1),
            (100, 0),
            (0, 0),
            (0, 5)
        ]
        
        for x, p in exception_data:
            with self.assertRaises(Exception):
                p_adic(x, p)

    def test_pollard_rho(self):
        """test pollard rho function"""

        for x in range(1, 100):
            if self.brute_is_prime(x):
                continue

            d = pollard_rho(x)

            self.assertEqual(x % d, 0)

            if x != 1:
                self.assertTrue(x != d)
                self.assertTrue(x != 1)
            

        with self.assertRaises(Exception):
            pollard_rho(0)

        with self.assertRaises(Exception):
            pollard_rho(-1)

    def test_factorize(self):
        """test factorization"""

        for x in range(1, 100):
            f = factorize(x)
            self.assertEqual(sorted(f), f)

            for p in f:
                self.assertTrue(self.brute_is_prime(p))
        
            self.assertEqual(reduce(mul, f, 1), x)

        with self.assertRaises(Exception):
            factorize(0)

        with self.assertRaises(Exception):
            factorize(-1)

    def test_factorize_exponent(self):
        """test factorize_exponent"""
        for x in range(1, 100):
            f = factorize_exponent(x)
            self.assertEqual(sorted(f), f)

            for p, e in f:
                self.assertTrue(self.brute_is_prime(p))
                self.assertTrue(e > 0)

            reductor = lambda val, pair: val * (pair[0] ** pair[1])
            self.assertEqual(reduce(reductor, f, 1), x)
        
        with self.assertRaises(Exception):
            factorize_exponent(0)

        with self.assertRaises(Exception):
            factorize_exponent(-1)

    def test_divisors(self):
        """test divisors"""

        for x in range(1, 100):
            d = divisors(x)

            self.assertEqual(d, sorted(d))

            for i in range(1, x+1):
                self.assertEqual(x % i == 0, i in d)

        with self.assertRaises(Exception):
            divisors(0)

        with self.assertRaises(Exception):
            divisors(-1)