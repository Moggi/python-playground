import unittest
import calendar


def isLeap(year):
    if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
        return True
    return False


class TestIsLeap(unittest.TestCase):

    def test_IsLeap(self):
        self.assertEqual(isLeap(2000), True)
        self.assertEqual(isLeap(2400), True)

        self.assertEqual(isLeap(1800), False)
        self.assertEqual(isLeap(1900), False)
        self.assertEqual(isLeap(1990), False)
        self.assertEqual(isLeap(2100), False)
        self.assertEqual(isLeap(2200), False)
        self.assertEqual(isLeap(2300), False)
        self.assertEqual(isLeap(2500), False)

    @unittest.skip('Execute this only if test_IsLeap works')
    def test_IsEqualCalendar(self):
        # 1900 <= y <= 10**5
        for i in range(1900, 10**5 + 1):
            with self.subTest(i=i):
                self.assertEqual(isLeap(i), calendar.isleap(i))

if __name__ == '__main__':
    unittest.main()
