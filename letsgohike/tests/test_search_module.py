"""ünittest module for search_module.py"""
import unittest
import pandas as pd
from unittest.mock import patch
from letsgohike.modules.search_module import SearchModule

class TestSearchModule(unittest.TestCase):
    """test cases for search_module"""
    @classmethod
    def setUpClass(cls):
        """Set up test data"""
        cls.search_module = SearchModule(csv_file=None)  # No real file needed

        # Mock the DataFrame directly
        data = {
            "Name": ["Trail A", "Trail B", "Trail C"],
            "Latitude": [37.7749, 34.0522, 40.7128],
            "Longitude": [-122.4194, -118.2437, -74.0060],
            "Difficulty": ["easy", "moderate", "difficult"],
            "Distance_Miles": [5.0, 10.5, 7.8],
            "elevation_gain": [500, 1500, 1000]
        }
        cls.search_module.trails = pd.DataFrame(data)  # Mock the dataset

    @patch("letsgohike.modules.search_module.Nominatim.geocode")
    def test_find_nearest_trails_valid_location(self, mock_geocode):
        """Test search with a valid location"""
        mock_geocode.return_value = type('obj', (object,), {"latitude": 37.7749, "longitude": -122.4194})

        results = self.search_module.find_nearest_trails(
            location="San Francisco, CA",
            difficulty="easy",
            length_range=(4, 6),
            elevation_range=(400, 600),
            max_distance_away=50
        )

        self.assertFalse(results.empty)
        self.assertEqual(len(results), 1)
        self.assertEqual(results.iloc[0]["Name"], "Trail A")

    @patch("letsgohike.modules.search_module.Nominatim.geocode")
    def test_find_nearest_trails_invalid_location(self, mock_geocode):
        """Test search with an invalid location"""
        mock_geocode.return_value = None

        results = self.search_module.find_nearest_trails(
            location="Invalid Place",
            difficulty="easy",
            length_range=(4, 6),
            elevation_range=(400, 600),
            max_distance_away=50
        )

        self.assertTrue(results.empty)

    def test_filter_by_difficulty(self):
        """Test filtering by difficulty"""
        results = self.search_module.find_nearest_trails(
            location="Los Angeles, CA",
            difficulty="moderate",
            length_range=(0, 20),
            elevation_range=(0, 5000),
            max_distance_away=100
        )

        self.assertEqual(len(results), 1)
        self.assertEqual(results.iloc[0]["Difficulty"], "moderate")

    def test_filter_by_length_range(self):
        """Test filtering by length range"""
        results = self.search_module.find_nearest_trails(
            location="San Francisco, CA",
            difficulty="easy",
            length_range=(6, 10),
            elevation_range=(0, 5000),
            max_distance_away=100
        )

        self.assertTrue(results.empty)  # Trail A is 5 miles, should be excluded

    def test_filter_by_elevation_gain(self):
        """Test filtering by elevation gain range"""
        results = self.search_module.find_nearest_trails(
            location="San Francisco, CA",
            difficulty="easy",
            length_range=(0, 10),
            elevation_range=(600, 800),
            max_distance_away=100
        )

        self.assertTrue(results.empty)  # No trails within elevation range

if __name__ == "__main__":
    unittest.main()
