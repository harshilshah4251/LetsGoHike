# pylint: disable=no-name-in-module
# pylint: disable=import-error
"""
Unit tests for the HikeMapModule class in letsgohike.modules.hike_map_module.
Validates display functionality under different conditions.
"""

import unittest
from unittest.mock import patch, MagicMock
import streamlit as st
import folium
from letsgohike.modules.hike_map_module import HikeMapModule


class TestHikeMapModule(unittest.TestCase):
    """Tests for the HikeMapModule class."""

    @patch("letsgohike.modules.hike_map_module.folium.Map", autospec=True)
    @patch("streamlit_folium.st_folium", autospec=True)
    @patch.object(st, "warning") 
    def test_display_with_valid_hike(self, mock_folium_map, mock_st_folium, _mock_warning):
        """
        Test display method with a valid hike:
        - Ensures the map is rendered with the correct coordinates.
        - Validates folium and streamlit_folium interactions.
        """

        # Ensure session_state key exists
        st.session_state.pop("selected_hike", None)
        st.session_state.selected_hike = {
            "name": "Trail A",
            "Latitude": 47.6072,
            "Longitude": -122.3324,
            "city_name": "Seattle",
            "state_name": "WA"
        }

        # Create instance of HikeMapModule
        hike_map_module = HikeMapModule()

        # Call the display method
        hike_map_module.display()

        # Assert folium.Map() is called correctly
        mock_folium_map.assert_called_once_with(location=[47.6072, -122.3324], zoom_start=12)

        # Assert st_folium renders the map
        mock_st_folium.assert_called_once()

#    @patch.object(st, "warning")
#    @patch("streamlit_folium.st_folium")
#    def test_display_no_selected_hike(self, _mock_st_folium, mock_warning):
#        """
#        Test display method when no hike is selected:
#        - Ensures a warning message is displayed.
#        """
#
#        st.session_state.pop("selected_hike", None)
#
#        hike_map_module = HikeMapModule()
#
#        hike_map_module.display()
#
#        mock_warning.assert_called_once_with(
#            "Please select a trail from the list to view its location on the map."
#        )

    @patch.object(st, "warning")
    @patch("streamlit_folium.st_folium")
    def test_display_with_invalid_location_data(self, _mock_st_folium, mock_warning):
        """
        Test display method when selected hike has invalid location data:
        - Verifies that a warning message is shown.
        """

        st.session_state.pop("selected_hike", None)
        st.session_state.selected_hike = {
            "name": "Mountain Trail",
            "Latitude": None,
            "Longitude": None,
            "city_name": "Seattle",
            "state_name": "WA"
        }

        hike_map_module = HikeMapModule()

        hike_map_module.display()

        mock_warning.assert_called_once_with("Selected hike does not have valid location data.")


if __name__ == "__main__":
    unittest.main()
