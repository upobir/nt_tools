import unittest
from nt_tools.mod_integer import *

class TestModInteger(unittest.TestCase):
    
    def setUp(self) ->None:
        __doc__
        pass

    def tearDown(self) -> None:
        __doc__
        M.default_mod = None

    def modint_equal(self, m: ModInteger, value: int, mod: int) -> None:
        """helper function assert modinteger value and mod"""
        self.assertEqual(m.value, value)
        self.assertEqual(m.mod, mod)

    def test_constructor(self) -> None:
        """test ModInteger constructor"""
        x: ModInteger

        x = M(5, 100)
        self.modint_equal(x, 5, 100)

        x = M(-4, 141)
        self.modint_equal(x, 137, 141)

        x = M(65, 65)
        self.modint_equal(x, 0, 65)

        with self.assertRaises(Exception):
            x = M(1)
        
        with self.assertRaises(Exception):
            x = M(1, 0)

        with self.assertRaises(Exception):
            x = M(1, -1)

        M.default_mod = 313
        x = M(314)
        self.modint_equal(x, 1, 313)

    def test_str_and_repr(self) -> None:
        """test str() and repr()"""
        x: ModInteger

        x = M(12, 111)
        self.assertEqual(repr(x), '< 12 (mod 111)>')
        self.assertEqual(str(x), '12')

    def test_equality(self) -> None:
        """test equality and non-equality"""
        x: ModInteger = M(1, 100)
        y: ModInteger = M(2, 99)

        self.assertFalse(x == y)
        self.assertTrue(x != y)

        y = M(2, 100)

        self.assertFalse(x == y)
        self.assertTrue(x != y)

        y = M(1, 99)

        self.assertFalse(x == y)
        self.assertTrue(x != y)

        y = M(1, 100)

        self.assertTrue(x == y)
        self.assertFalse(x != y)

        self.assertFalse(x == 1)
        self.assertTrue(x != 1)

    def test_add(self) -> None:
        """test addition"""
        x: ModInteger
        y: ModInteger

        x = M(52, 100)
        y = M(68, 100)

        z: ModInteger = x+y
        self.modint_equal(z, 20, 100)

        z = x+111
        self.modint_equal(z, 63, 100)

        z = x+(-111)
        self.modint_equal(z, 41, 100)

        y = M(68, 99)

        with self.assertRaises(Exception):
            x+y

    def test_subtract(self) -> None:
        """test subtraction"""
        x: ModInteger
        y: ModInteger

        x = M(12, 100)
        y = M(30, 100)

        z: ModInteger = y-x
        self.modint_equal(z, 18, 100)

        z= x-y
        self.modint_equal(z, 82, 100)

        z = x - 1
        self.modint_equal(z, 11, 100)

        z = x - (-1)
        self.modint_equal(z, 13, 100)

        y = M(1, 99)

        with self.assertRaises(Exception):
            x-y

    def test_multiplication(self) -> None:
        """test multiplication"""
        x: ModInteger
        y: ModInteger

        x = M(12, 101)
        y = M(30, 101)

        z: ModInteger
        z = x*y
        self.modint_equal(z, 57, 101)

        z = x * 50
        self.modint_equal(z, 95, 101)

        z = x * (-50)
        self.modint_equal(z, 6, 101)

        y = M(1, 99)

        with self.assertRaises(Exception):
            x * y

    def test_division(self) -> None:
        """test inverse, division"""

        x: ModInteger

        x = M(31, 100)
        self.assertTrue(x.is_invertible())

        x = M(25, 100)
        self.assertFalse(x.is_invertible())

        x = M(0, 100)
        self.assertFalse(x.is_invertible())

        x = M(31, 100)
        y: ModInteger = x.inverse()

        self.modint_equal(x*y, 1, 100)

        y = M(27, 100)

        z: ModInteger = x / y

        self.modint_equal(z*y, 31, 100)

        y = M(27, 128)
        with self.assertRaises(Exception):
            x / y

        y = M(2, 100)
        with self.assertRaises(Exception):
            x / y

    def test_power(self) -> None:
        """test power"""
        x: ModInteger = M(10, 107)

        for i in range(0, 10):
            y: ModInteger = x ** i
            z: ModInteger = M(x.value ** i, x.mod)

            self.modint_equal(y, z.value, z.mod)

        xinv: ModInteger = x.inverse()
        for i in range(-10, 0):
            y = x ** i
            z = M(xinv.value ** -i, xinv.mod)

            self.modint_equal(y, z.value, z.mod)

        x = M(10, 100)
        with self.assertRaises(Exception):
            x ** -1

        self.modint_equal(x**1, 10, 100)

    def test_guess_int_from_modint(self):
        """test guess_int_from_modint"""
        x: ModInteger = M(5, 100)
        self.assertEqual(guess_int_from_modint(x), 5)

        x = M(-5, 100)
        self.assertEqual(guess_int_from_modint(x), -5)

        x = M(0, 100)
        self.assertEqual(guess_int_from_modint(x), 0)

        x = M(50, 100)
        self.assertEqual(guess_int_from_modint(x), 50)

