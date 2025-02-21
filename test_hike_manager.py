# test_hike_manager.py

import unittest

from hike import Hike
from hike_manager import HikeManager


class TestHikeManager(unittest.TestCase):
    
    def setUp(self):
        """Set up a list of sample hikes for testing."""
        self.hikes = [
            Hike("Mountain Trail", "Easy", "Sunny", "Morning"),
            Hike("Forest Path", "Moderate", "Cloudy", "Afternoon"),
            Hike("Lake View", "Hard", "Rainy", "Evening"),
            Hike("Sunset Ridge", "Easy", "Sunny", "Evening"),
        ]
        self.hike_manager = HikeManager(self.hikes)
    
    def test_suggest_hike_exact_match(self):
        """Test that the function returns the correct hike when preferences match exactly."""
        preferences = {
            "difficulty": "Easy",
            "weather": "Sunny",
            "time_of_day": "Morning"
        }
        result = self.hike_manager.suggest_hike(preferences)
        self.assertEqual(result, ["Mountain Trail"])

    def test_suggest_hike_multiple_matches(self):
        """Test that the function returns multiple hikes when preferences match multiple hikes."""
        preferences = {
            "difficulty": "Easy",
            "weather": "Sunny",
            "time_of_day": "Evening"
        }
        result = self.hike_manager.suggest_hike(preferences)
        self.assertEqual(result, ["Sunset Ridge"])

    def test_suggest_hike_no_match(self):
        """Test that the function returns an empty list when no hikes match the preferences."""
        preferences = {
            "difficulty": "Hard",
            "weather": "Sunny",
            "time_of_day": "Morning"
        }
        result = self.hike_manager.suggest_hike(preferences)
        self.assertEqual(result, [])

    def test_suggest_hike_partial_match(self):
        """Test that the function doesn't return hikes if there’s a partial match."""
        preferences = {
            "difficulty": "Easy",
            "weather": "Sunny"
        }
        result = self.hike_manager.suggest_hike(preferences)
        self.assertEqual(result, ["Mountain Trail", "Sunset Ridge"])

    def test_suggest_hike_empty_preference(self):
        """Test that the function returns all hikes when no preferences are provided."""
        preferences = {}
        result = self.hike_manager.suggest_hike(preferences)
        self.assertEqual(result, [
            "Mountain Trail", 
            "Forest Path", 
            "Lake View", 
            "Sunset Ridge"
        ])
        
    def test_suggest_hike_invalid_preference(self):
        """Test that the function handles invalid preferences gracefully."""
        preferences = {
            "difficulty": "Very Hard",  # Invalid difficulty
            "weather": "Sunny",
            "time_of_day": "Morning"
        }
        result = self.hike_manager.suggest_hike(preferences)
        self.assertEqual(result, [])

    def test_suggest_hike_case_sensitivity(self):
        """Test that the function is case-sensitive for preferences."""
        preferences = {
            "difficulty": "easy",  # lowercase instead of "Easy"
            "weather": "Sunny",
            "time_of_day": "Morning"
        }
        result = self.hike_manager.suggest_hike(preferences)
        self.assertEqual(result, [])

if __name__ == "__main__":
    unittest.main()
