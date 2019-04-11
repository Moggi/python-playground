import unittest


def solve(s):
    sx = s[0].upper()
    for i in range(1, len(s)):
        if s[i].isalpha() and s[i-1] == ' ':
            sx += s[i].upper()
        else:
            sx += s[i]
    return sx


def solve2(s):
    sx = ''
    p = s.find(' ')
    while p != -1:
        s = s.capitalize()
        sx += s[:p+1]
        s = s[p+1:]
        p = s.find(' ')
    s = s.capitalize()
    sx += s
    return sx


class TestCaptalize(unittest.TestCase):

    def test_capitalize(self):
        s = [
            (
                'a long text that needs to get capitalized',
                'A Long Text That Needs To Get Capitalized'
            ),
            ('a', 'A'),
            ('chris alan', 'Chris Alan'),
            ('12abc', '12abc'),
            (' Aab c', ' Aab C'),
            ('  aa bb  cc    ', '  Aa Bb  Cc    '),
        ]
        for i in s:
            self.subTest(i=i)
            self.assertEqual(solve2(i[0]), i[1])


if __name__ == '__main__':
    unittest.main()
