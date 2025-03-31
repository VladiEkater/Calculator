import unittest
from calculator import Calculator
from utils import is_number
class TestCalculator(unittest.TestCase):
    def test_is_number_with_valid_input(self):
        self.assertTrue(is_number('123'))
        self.assertTrue(is_number('123.456'))
        self.assertTrue(is_number('-123'))
        self.assertTrue(is_number('0'))
    def test_is_number_with_invalid_input(self):
        self.assertFalse(is_number('abc'))
        self.assertFalse(is_number('123abc'))
        self.assertFalse(is_number(''))
    def test_calculator_addition(self):
        calc = Calculator()
        result = calc.calculate(3, '+', 4)
        self.assertEqual(result, 7)
    def test_calculator_subtraction(self):
        calc = Calculator()
        result = calc.calculate(10, '-', 4)
        self.assertEqual(result, 6)
    def test_calculator_multiplication(self):
        calc = Calculator()
        result = calc.calculate(3, '*', 5)
        self.assertEqual(result, 15)
    def test_calculator_division(self):
        calc = Calculator()
        result = calc.calculate(10, '/', 2)
        self.assertEqual(result, 5)
    def test_calculator_division_by_zero(self):
        calc = Calculator()
        result = calc.calculate(10, '/', 0)
        self.assertIsNone(result)
    def test_calculator_invalid_operation(self):
        calc = Calculator()
        result = calc.calculate(10, '^', 2)
        self.assertIsNone(result)
if __name__ == '__main__':
    unittest.main()
