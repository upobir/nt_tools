import unittest
from nt_tools.factorization import *

class TestFactorization(unittest.TestCase):
    def setUp(self) ->None:
        __doc__
        pass

    def tearDown(self) -> None:
        __doc__
        pass

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