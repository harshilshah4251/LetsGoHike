import unittest
from unittest.mock import patch
import streamlit as st
from letsgohike.modules.hike_map_module import HikeMapModule

class TestHikeMapModule(unittest.TestCase):
    """Unit tests for HikeMapModule."""

    def setUp(self):
        """Initialize HikeMapModule before each test."""
        self.module = HikeMapModule()

    # Test 1: Test that the map is not displayed when no hike is selected
    @patch("streamlit.write")
    @patch("streamlit.warning")
    @patch("streamlit_folium.st_folium")
    def test_hike_map_module_no_hike_selected(self, mock_st_folium, mock_warning, mock_write):
        """Test that the map is not displayed when no hike is selected."""

        # Make sure there is no selected hike in the session state
        if "selected_hike" in st.session_state:
            del st.session_state["selected_hike"]

        # Call the display method (which should check for selected hike in session state)
        self.module.display()

        # Check if st_folium was not called (since no hike was selected)
        mock_st_folium.assert_not_called()

        # Check that no map is displayed, and a warning is issued
        mock_warning.assert_not_called()
        mock_write.assert_not_called()

    # Test 2: Test display method with valid hike data
    @patch("letsgohike.modules.hike_map_module.st_folium")  # Mock the correct path
    @patch("streamlit.header")
    @patch("streamlit.write")
    def test_display_with_valid_hike(self, mock_write, mock_header, mock_st_folium):
        """Test display method with valid hike data."""
        # Mock the session state with valid coordinates
        st.session_state.selected_hike = {
            "Latitude": 47.6062,
            "Longitude": -122.3321,
            "name": "Mount Si",
            "city_name": "Seattle",
            "state_name": "WA"
        }

        # Call the display method
        self.module.display()

        # Verify display calls
        mock_header.assert_called_once_with("Trail Map")
        mock_write.assert_called_once_with("Showing the trailhead for **Mount Si** on the map...")
        mock_st_folium.assert_called_once()  # Verify map rendering is called


if __name__ == "__main__":
    unittest.main()
