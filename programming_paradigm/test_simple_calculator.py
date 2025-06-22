import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):

    def setUp(self):
        """Create a new calculator instance before each test."""
        self.calc = SimpleCalculator()

    # --- Tests for addition ---
    def test_addition_with_positive_numbers(self):
        self.assertEqual(self.calc.add(2, 3), 5)

    def test_addition_with_negative_numbers(self):
        self.assertEqual(self.calc.add(-2, -3), -5)

    def test_addition_with_zero(self):
        self.assertEqual(self.calc.add(0, 5), 5)
        self.assertEqual(self.calc.add(5, 0), 5)

    # --- Tests for subtraction ---
    def test_subtraction_with_positive_numbers(self):
        self.assertEqual(self.calc.subtract(10, 4), 6)

    def test_subtraction_with_negative_result(self):
        self.assertEqual(self.calc.subtract(4, 10), -6)

    def test_subtraction_with_zero(self):
        self.assertEqual(self.calc.subtract(0, 5), -5)
        self.assertEqual(self.calc.subtract(5, 0), 5)

    # --- Tests for multiplication ---
    def test_multiplication_with_positive_numbers(self):
        self.assertEqual(self.calc.multiply(4, 3), 12)

    def test_multiplication_with_negative_numbers(self):
        self.assertEqual(self.calc.multiply(-4, 3), -12)

    def test_multiplication_with_zero(self):
        self.assertEqual(self.calc.multiply(0, 5), 0)
        self.assertEqual(self.calc.multiply(5, 0), 0)

    # --- Tests for division ---
    def test_division_with_positive_numbers(self):
        self.assertEqual(self.calc.divide(10, 2), 5)

    def test_division_with_negative_result(self):
        self.assertEqual(self.calc.divide(10, -2), -5)

    def test_division_by_zero(self):
        self.assertIsNone(self.calc.divide(10, 0))

    def test_division_zero_numerator(self):
        self.assertEqual(self.calc.divide(0, 5), 0)

if __name__ == '__main__':
    unittest.main()
