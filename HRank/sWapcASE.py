import unittest


def swap_string(s):
    sx = ''
    for i in range(len(s)):
        if s[i].islower():
            sx = sx + s[i].upper()
        else:
            sx = sx + s[i].lower()
    return sx


class TestSwap(unittest.TestCase):

    def test_swap(self):
        s = [
            'Az',
            'zA',
            'Www.HackerRank.com',
            'Pythonist 2'
        ]
        for i in s:
            self.subTest(i=i)
            self.assertEqual(swap_string(i), i.swapcase())

if __name__ == '__main__':
    unittest.main()
