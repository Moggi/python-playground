import unittest
import textwrap


def wrap(string, max_width):
    return '\n'.join(textwrap.wrap(string, max_width, replace_whitespace=False,
                                   drop_whitespace=False))


class TestWrap(unittest.TestCase):

    def test_wrap(self):
        s = [
            ('ABCDEFGHI', 'ABCD\nEFGH\nI'),
            (
                'ABCDEFGHIJKLIMNOQRSTUVWXYZ',
                'ABCD\nEFGH\nIJKL\nIMNO\nQRST\nUVWX\nYZ'
            ),
            ('  AA  ', '  AA\n  ')
        ]
        for i in s:
            self.subTest(i=i)
            self.assertEqual(wrap(i[0], 4), i[1])


if __name__ == "__main__":
    unittest.main()
    # string, max_width = input(), int(input())
    # result = wrap(string, max_width)
    # print(result)
