import unittest


class TestCalc(unittest.TestCase):

    def test_dimensions(self):
        N = 2
        l = generate_cuboid_dimensions(1, 1, 1, N)
        for i in range(len(l)):
            with self.subTest(i=i):
                self.assertNotEqual(l[i][0]+l[i][0]+l[i][0], N)

        l = generate_cuboid_dimensions(2, 2, 2, N)
        for i in range(len(l)):
            with self.subTest(i=i):
                self.assertNotEqual(l[i][0]+l[i][0]+l[i][0], N)


def generate_cuboid_dimensions(X, Y, Z, N):
    return [
        [i, j, k]
        for i in range(X + 1) for j in range(Y + 1) for k in range(Z + 1)
        if (i+j+k != N)
    ]


# X = int(input())
# Y = int(input())
# Z = int(input())
# N = int(input())

if __name__ == "__main__":
    unittest.main()
# print(generate_cuboid_dimensions(X, Y, Z, N))
