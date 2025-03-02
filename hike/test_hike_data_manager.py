import unittest
import pandas as pd
from hike_data_manager import filter_hikes

class TestHikeDataManager(unittest.TestCase):

    def setUp(self):
        """Set up a sample DataFrame for testing"""
        self.df = pd.DataFrame([
            {"name": "Hike A", "Difficulty": "Easy", "elevation_gain": 500},
            {"name": "Hike B", "Difficulty": "Moderate", "elevation_gain": 1500},
            {"name": "Hike C", "Difficulty": "Hard", "elevation_gain": 3000},
            {"name": "Hike D", "Difficulty": "Moderate", "elevation_gain": 2500},
            {"name": "Hike E", "Difficulty": "Easy", "elevation_gain": 800},
        ])

    def test_filter_by_difficulty(self):
        """Test filtering by difficulty level"""
        filtered_df = filter_hikes(self.df, "Moderate", (0, 5000))
        self.assertEqual(len(filtered_df), 2)  # Expecting two "Moderate" hikes
        self.assertTrue(all(filtered_df["Difficulty"] == "Moderate"))

    def test_filter_by_elevation(self):
        """Test filtering by elevation gain"""
        filtered_df = filter_hikes(self.df, "All", (1000, 3000))
        self.assertEqual(len(filtered_df), 3)  # Expecting 3 hikes within elevation range
        self.assertTrue(all(1000 <= filtered_df["elevation_gain"]) and all(filtered_df["elevation_gain"] <= 3000))

    def test_filter_by_difficulty_and_elevation(self):
        """Test filtering by both difficulty and elevation"""
        filtered_df = filter_hikes(self.df, "Moderate", (1000, 2000))
        self.assertEqual(len(filtered_df), 1)  # Expecting only one hike (Hike B)
        self.assertEqual(filtered_df.iloc[0]["name"], "Hike B")

    def test_filter_all_difficulties(self):
        """Test when difficulty is 'All' to ensure no unnecessary filtering"""
        filtered_df = filter_hikes(self.df, "All", (0, 5000))
        self.assertEqual(len(filtered_df), len(self.df))  # Expecting all hikes

if __name__ == "__main__":
    unittest.main()
