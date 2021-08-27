import unittest
from nt_tools.diophantine import *
from nt_tools.mod_integer import ModInteger
from typing import Tuple, List

class TestDiophantine(unittest.TestCase):
    def setUp(self) ->None:
        __doc__
        pass

    def tearDown(self) -> None:
        __doc__
        pass

    def bezout_check(self, a: int, x: int, b: int, y: int, g: int) -> None:
        self.assertEqual(g, gcd(a, b))
        self.assertTrue(abs(x) <= max(1, abs(b)/g))
        self.assertTrue(abs(y) <= max(1, abs(a)/g))
        self.assertEqual(a*x+b*y, g)

    def test_bezout(self) -> None:
        """test bezout function"""

        inputs: List[Tuple[int, int]] = [
            (50, 35),
            (-50, 35),
            (-50, -35),
            (-50, -35),
            (50, 0),
            (0, 50),
            (-50, 0),
            (0, -50),
        ]

        for a, b in inputs:
            x, y, g = bezout(a, b)
            self.bezout_check(a, x, b, y, g)

        with self.assertRaises(Exception):
            bezout(0, 0)

    def brute_lcm(self, a, b):
        """brute funtion to find lcm"""
        if a == 0 or b == 0:
            return 0

        m = 1
        while m % a != 0 or m % b != 0:
            m += 1
        
        return m

    def test_lcm(self) -> None:
        """test lcm function"""
        for i in range(-10, 10):
            for j in range(-10, 10):
                if i == 0 and j == 0:
                    continue
                l = lcm(i, j)
                self.assertTrue(l >= 0)
                self.assertEqual(l, self.brute_lcm(i, j))

        with self.assertRaises(Exception):
            lcm(0, 0)

    def test_crt(self) -> None:
        """test crt function"""
        a = 6
        b = 9
        c = 14

        for i in range(1, a+1):
            for j in range(1, b+1):
                for k in range(1, c+1):
                    res = crt(ModInteger(i, a), ModInteger(j, b), ModInteger(k, c))

                    if i % 2 == k % 2 and i % 3 == j % 3:
                        self.assertFalse(res is None, f"{i}, {j}, {k}")

                        m = self.brute_lcm(self.brute_lcm(a, b), c)
                        self.assertEqual(m, res.mod)
                        for x in range(0, m):
                            if x % a == i and x % j == b and x % k == c:
                                self.assertEqual(x, res.value)
                    else:
                        self.assertTrue(res is None)

    def test_diophantine(self) -> None:
        """test diophantine function"""
        for a in range(-20, 20):
            for b in range(-20, 20):
                for c in range(-20, 20):
                    solution = diophantine(a, b, c)

                    if solution is None:
                        if a == 0 and b == 0:
                            self.assertNotEqual(c, 0)
                        else:
                            self.assertNotEqual(c % gcd(a, b), 0)
                    else:
                        x, y = solution
                        self.assertEqual(a*x+b*y, c)