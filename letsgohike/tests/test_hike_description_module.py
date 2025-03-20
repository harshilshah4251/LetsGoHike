import unittest
from unittest.mock import patch, MagicMock
import streamlit as st

# Import the module to test (adjust the import as necessary)
from hike_description_module import HikeDescriptionModule

class TestHikeDescriptionModule(unittest.TestCase):
    # ----- Tests for get_trek_description -----
    @patch("hike_description_module.genai.GenerativeModel")
    @patch("hike_description_module.genai.configure")
    def test_get_trek_description_success(self, mock_configure, mock_generative_model):
        # Set up a fake model instance with a fake response
        fake_model_instance = MagicMock()
        fake_response = MagicMock()
        fake_response.text = "This is a fake trek description."
        fake_model_instance.generate_content.return_value = fake_response
        mock_generative_model.return_value = fake_model_instance

        module = HikeDescriptionModule()
        result = module.get_trek_description("Everest", "fake_api_key")
        self.assertEqual(result, "This is a fake trek description.")

    @patch("hike_description_module.genai.GenerativeModel")
    @patch("hike_description_module.genai.configure")
    def test_get_trek_description_exception(self, mock_configure, mock_generative_model):
        # Simulate an exception when calling generate_content
        fake_model_instance = MagicMock()
        fake_model_instance.generate_content.side_effect = Exception("Test error")
        mock_generative_model.return_value = fake_model_instance

        module = HikeDescriptionModule()
        result = module.get_trek_description("Everest", "fake_api_key")
        self.assertTrue(result.startswith("Issues with genai"))
        self.assertIn("Test error", result)

    # ----- Tests for display -----
    @patch('streamlit.write')
    @patch('streamlit.session_state', new_callable=dict)
    @patch.object(HikeDescriptionModule, 'get_trek_description')
    def test_display_with_valid_description(self, mock_get_trek_description, mock_session_state, mock_st_write):
        # Set up a fake session state with a selected hike.
        fake_hike = {'city_name': 'Kathmandu', 'name': 'Everest'}
        mock_session_state['selected_hike'] = fake_hike
        
        # Simulate get_trek_description returning a valid description.
        mock_get_trek_description.return_value = "Detailed trek description."

        module = HikeDescriptionModule()
        module.display()

        # Verify that st.write was called for both the formatted trek and the description.
        expected_formatted = "Everest,Kathmandu "
        mock_st_write.assert_any_call(expected_formatted)
        mock_st_write.assert_any_call("Detailed trek description.")

    @patch('streamlit.write')
    @patch('streamlit.session_state', new_callable=dict)
    @patch.object(HikeDescriptionModule, 'get_trek_description')
    def test_display_with_no_description(self, mock_get_trek_description, mock_session_state, mock_st_write):
        # Set up a fake session state with a selected hike.
        fake_hike = {'city_name': 'Kathmandu', 'name': 'Everest'}
        mock_session_state['selected_hike'] = fake_hike

        # Simulate get_trek_description returning an empty string.
        mock_get_trek_description.return_value = ""

        module = HikeDescriptionModule()
        module.display()

        # Verify that st.write was called with the formatted trek and then "No description available".
        expected_formatted = "Everest,Kathmandu "
        mock_st_write.assert_any_call(expected_formatted)
        mock_st_write.assert_any_call("No description available")

    @patch('streamlit.write')
    @patch('streamlit.session_state', new_callable=dict)
    def test_display_no_selected_hike(self, mock_session_state, mock_st_write):
        # Ensure no selected_hike is present in session_state.
        if "selected_hike" in mock_session_state:
            del mock_session_state["selected_hike"]

        module = HikeDescriptionModule()
        module.display()

        # When no selected_hike exists, st.write should not be called.
        mock_st_write.assert_not_called()

if __name__ == '__main__':
    unittest.main()
