import unittest


def has_any(s):
    n = False
    a = False
    d = False
    l = False
    u = False
    for i in s:
        if not n and i.isalnum():
            n = True
        if not a and i.isalpha():
            a = True
        if not d and i.isdigit():
            d = True
        if not l and i.islower():
            l = True
        if not u and i.isupper():
            u = True
    return n, a, d, l, u


class TestString(unittest.TestCase):

    def test_has_any(self):
        s = [
            ('qA2', (True, True, True, True, True)),
            ('ABCD123#', (True, True, True, False, True))
        ]
        for i in s:
            self.subTest(i=i)
            self.assertEqual(has_any(i[0]), i[1])


if __name__ == "__main__":
    unittest.main()
