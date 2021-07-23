import unittest
from nt_tools.diophantine import *
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