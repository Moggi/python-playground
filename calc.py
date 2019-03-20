import unittest


def add(_x, _y):
    """Return the sum of two objects.
    Expect both parameters to be integer or float.
    """
    return _x + _y


def subtract(_x, _y):
    """Return the subtraction of two objects.
    Expect both parameters to be integer or float.
    """
    return _x - _y


def multiply(_x, _y):
    """Return the multiplication of two objects.
    Expect both parameters to be integer or float.
    """
    return _x * _y


def divide(_x, _y):
    """Return the division of two objects.
    Expect both parameters to be integer or float.
    Raise ValueError in case the second been zero.
    """
    if _y == 0:
        raise ValueError('Can not dive by zero')
    return _x / _y


class TestCalc(unittest.TestCase):

    def test_add(self):
        """Tests the expected cases for add(a, b)"""
        self.assertEqual(add(10, 5), 15)
        self.assertEqual(add(-1, 1), 0)
        self.assertEqual(add(-2, -3), -5)

    def test_subtract(self):
        """Tests the expected cases for subtract(a, b)"""
        self.assertEqual(subtract(10, 5), 5)
        self.assertEqual(subtract(-1, 1), -2)
        self.assertEqual(subtract(-2, -3), 1)

    def test_multiply(self):
        """Tests the expected cases for multiply(a, b)"""
        self.assertEqual(multiply(10, 5), 50)
        self.assertEqual(multiply(-1, 1), -1)
        self.assertEqual(multiply(-2, -3), 6)

    def test_divide(self):
        """Tests the expected cases for divide(a, b) including the exception"""
        self.assertEqual(divide(10, 5), 2)
        self.assertEqual(divide(-1, 1), -1)
        self.assertEqual(divide(-2, -3), 2/3)
        self.assertRaises(ValueError, divide, -1, 0)
        with self.assertRaises(ValueError):
            divide(10, 0)


if __name__ == '__main__':
    unittest.main()
