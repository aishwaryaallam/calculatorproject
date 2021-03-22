import unittest
import csv
import math


class calculator():
    def addition(self, a, b):
        return a + b

    def subtraction(self, a, b):
        return a - b

    def multiplication(self, a, b):
        return a * b

    def division(self, a, b):
        return a / b

    def square(self, a):
        return a ** 2

    def squareRoot(self, a):
        return math.sqrt(a)


class TestCalC(unittest.TestCase):
    calculator = None

    @classmethod
    def setUpClass(cls):
        cls.calculator = calculator()

    def test_addition(self):
        a = []
        b = []
        ans = []
        with open('Unit Test Addition.csv') as file:
            csv_reader = csv.reader(file, delimiter=',')
            line = 0
            for row in csv_reader:
                if line != 0:
                    a.append(float(row[0]))
                    b.append(float(row[1]))
                    ans.append(float(row[2]))
                line += 1

        for i in range(0, len(a)):
            self.assertEqual(self.calculator.addition(a[i], b[i]), ans[i])
        print("Addition all test case passed")


if __name__ == '__main__':
    unittest.main(verbosity=2)