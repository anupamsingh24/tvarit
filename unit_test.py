import task1
import unittest

class Task1Test(unittest.TestCase):
    def test1(self):
        self.assertEqual(task1.sumOfThreeNumbers(1,2,3), 6)

    def test2(self):
        self.assertEqual(task1.sumOfThreeNumbers(13, 17, 19), 0)

    def test3(self):
        self.assertEqual(task1.sumOfThreeNumbers(15, 16, 13), 31)

    def test4(self):
        self.assertEqual(task1.sumOfThreeNumbers(-1, -2, -3), -6)

if __name__ == '__main__':
    unittest.main()