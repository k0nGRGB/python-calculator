import unittest
from calculator import Calculator

class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.calc = Calculator()

    def test_add(self):
        self.assertEqual(self.calc.add(1, 2), 3)

    # Add the following test methods to the TestCalculator class:

    # Test cases for add
    def test_add_negative(self):
        self.assertEqual(self.calc.add(3, -2), 1)

    def test_add_zero(self):
        self.assertEqual(self.calc.add(0, 1), 1)


    # Test cases for substract
    def test_subtract_positive(self):
        self.assertEqual(self.calc.subtract(3, 2), 1)
    
    def test_subtract_negative(self):
        self.assertEqual(self.calc.subtract(-3, -2), -1)

    # Test cases for multiply
    def test_multiply_positive(self):
        self.assertEqual(self.calc.multiply(3, 2), 6)

    def test_multiply_negative(self):
        self.assertEqual(self.calc.multiply(3, -2), -6)

    def test_multiply_decimal(self):
        self.assertEqual(self.calc.multiply(3, 1.5), 4.5)

    def test_multiply_double_negative(self):
        self.assertEqual(self.calc.multiply(-3, -2), 6)

        # Test cases for divide
    def test_divide_positive(self):
        self.assertEqual(self.calc.divide(2, 1), 2)

    def test_divide_negative(self):
        self.assertEqual(self.calc.divide(-2, 1), -2)

    def test_divide_by_zero(self):
        self.assertEqual(self.calc.divide(2, 0), 100000000)

        # Test cases for modulo
    def test_modulo(self):
        self.assertEqual(self.calc.modulo(3, 2), 1)

    def test_modulo_equal(self):
        self.assertEqual(self.calc.modulo(3, 3), 0)

    def test_modulo_a_less_than_b(self):
        self.assertEqual(self.calc.modulo(2, 3), 2)

    def test_modulo_by_zero(self):
        self.assertEqual(self.calc.modulo(2, 0), 100000000)

    

if __name__ == '__main__':
    unittest.main()