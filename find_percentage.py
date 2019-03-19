import unittest


def average(*numbers):
    return float(sum(numbers)) / max(len(numbers), 1)


def get_n_students(N):
    students = {}
    for i in range(N):
        inp = raw_input().split(' ')
        students[inp[0]] = int(inp[1]), int(inp[2]), int(inp[3])
    return students


def get_students():
    N = int(input())
    return get_n_students(N)


class TestCalc(unittest.TestCase):

    def test_average(self):
        self.assertEqual(average(10, 5), 7.5)
        self.assertEqual(average(10, 10), 10)
        self.assertEqual(average(-1, 10), 4.5)
        self.assertEqual(average(0, 0), 0)
        self.assertEqual(average(-1, 1), 0)

    @unittest.skip('Test the average function before')
    def test_students(self):
        students = get_students()
        self.assertIsInstance(students, dict)

        student = raw_input()
        self.assertIsInstance(students[student], tuple)


if __name__ == '__main__':
    unittest.main()
    # students = get_students()
    # student = raw_input()
    # avg = average(*students[student])
    # print('{:.2f}'.format(avg))
