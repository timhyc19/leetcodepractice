import unittest
from code_directory.my_calculations import Calculations

"""
To run python unit test, call
>>> python -m unittest
"""

class TestCalculations(unittest.TestCase):

    """
    setUp is same as declaring the following class above:
    @classmethod
    def setUpClass(self):
        self.calculation = Calculations(8, 2)

    """
    def setUp(self):
        self.calculations = Calculations(8, 2)

    def test_sum(self):
        self.assertEqual(self.calculations.get_sum(), 10, 'The sum is wrong.')

    def test_difference(self):
        self.assertEqual(self.calculations.get_difference(), 6, 'The difference is wrong.')

    def test_product(self):
        self.assertEqual(self.calculations.get_product(), 16, 'The product is wrong.')

    def test_quotient(self):
        self.assertEqual(self.calculations.get_quotient(), 4, 'The quotient is wrong.')

if __name__ == '__main__':
    unittest.main()