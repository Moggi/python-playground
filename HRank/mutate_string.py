import unittest


def mutate_string(string, position, character):
    return string[:position] + character + string[position+1:]


class TestMutation(unittest.TestCase):

    def test_mutate(self):
        s = [
            ('abracadabra', 5, 'K', 'abracKdabra'),
            ('   ', 1, 'K', ' K '),
            ('? ', 0, '!', '! '),
        ]
        for i in s:
            self.subTest(i=i)
            self.assertEqual(mutate_string(i[0], i[1], i[2]), i[3])


if __name__ == '__main__':
    unittest.main()
    # s = input()
    # i, c = input().split()
    # s_new = mutate_string(s, int(i), c)
    # print(s_new)
