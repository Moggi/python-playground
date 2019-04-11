from fractions import Fraction
from functools import reduce


def product(fracs):
    t = reduce(lambda x, y: x*y, fracs)
    return t.numerator, t.denominator


def init():
    fracs = []
    for _ in range(int(input())):
        fracs.append(Fraction(*map(int, input().split())))
    return product(fracs)


if __name__ == '__main__':
    tests = [
        (
            [Fraction('1/2'), Fraction('3/4'), Fraction('10/6')],
            Fraction(5, 8)
        ),
        (
            [Fraction('1/2')],
            Fraction(1, 2)
        ),
        (
            [Fraction('8/2'), Fraction('9/4'), Fraction('7/6')],
            Fraction(21, 2)
        ),
    ]
    for i in tests:
        assert product(i[0]) == (i[1].numerator, i[1].denominator)
