import unittest
from cityCountry import format_city_country

class TestCityFunctions(unittest.TestCase):
    def test_city_country(self):
        """Test that the function correctly formats city and country."""
        result = format_city_country('santiago', 'chile')
        self.assertEqual(result, 'Santiago, Chile')

if __name__ == '__main__':
    unittest.main()
