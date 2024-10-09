import unittest
from population import format_city_country

class TestCityFunctions(unittest.TestCase):
    def test_city_country(self):
        """Test that the function correctly formats city and country without population."""
        result = format_city_country('santiago', 'chile')
        self.assertEqual(result, 'Santiago, Chile')

    def test_city_country_population(self):
        """Test that the function correctly formats city and country with population."""
        result = format_city_country('santiago', 'chile', population=5000000)
        self.assertEqual(result, 'Santiago, Chile – population 5000000')

if __name__ == '__main__':
    unittest.main()