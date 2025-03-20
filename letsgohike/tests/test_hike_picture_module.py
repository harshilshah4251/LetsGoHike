import unittest
from unittest.mock import patch, MagicMock
import requests


#from hike_picture_module import HikePictureModule
from letsgohike.modules.hike_picture_module import HikePictureModule

class TestHikePictureModule(unittest.TestCase):

    # ----- Tests for get_trek_image -----

    @patch('requests.get')
    def test_get_trek_image_success(self, mock_get):
        # Simulate a successful API response with one image link.
        fake_response = MagicMock()
        fake_response.raise_for_status.return_value = None
        fake_response.json.return_value = {
            "items": [{"link": "http://example.com/image.jpg"}]
        }
        mock_get.return_value = fake_response

        module = HikePictureModule()
        result = module.get_trek_image("Everest", "fake_api_key", "fake_cse_id")
        self.assertEqual(result, "http://example.com/image.jpg")

    @patch('requests.get')
    def test_get_trek_image_request_exception(self, mock_get):
        # Simulate a network exception from requests.get.
        mock_get.side_effect = requests.exceptions.RequestException("Network error")
        module = HikePictureModule()
        result = module.get_trek_image("Everest", "fake_api_key", "fake_cse_id")
        self.assertTrue(result.startswith("Error Occurred"))
        self.assertIn("Network error", result)

    @patch('requests.get')
    def test_get_trek_image_json_error(self, mock_get):
        # Simulate an API response that includes an "error" in its JSON.
        fake_response = MagicMock()
        fake_response.raise_for_status.return_value = None
        fake_response.json.return_value = {
            "error": {"message": "API error occurred"}
        }
        mock_get.return_value = fake_response

        module = HikePictureModule()
        result = module.get_trek_image("Everest", "fake_api_key", "fake_cse_id")
        self.assertEqual(result, "Error Occurred: API error occurred")

    @patch('requests.get')
    def test_get_trek_image_no_items(self, mock_get):
        # Simulate a response where no items are returned.
        fake_response = MagicMock()
        fake_response.raise_for_status.return_value = None
        fake_response.json.return_value = {
            "items": []
        }
        mock_get.return_value = fake_response

        module = HikePictureModule()
        result = module.get_trek_image("Everest", "fake_api_key", "fake_cse_id")
        self.assertEqual(result, "No image found for this trek.")

    # ----- Tests for display method -----
    # For display, we need to simulate Streamlit's session_state, st.write, and st.markdown.
    @patch('streamlit.markdown')
    @patch('streamlit.write')
    @patch('streamlit.session_state', new_callable=dict)
    @patch.object(HikePictureModule, 'get_trek_image')
    def test_display_valid_image(self, mock_get_trek_image, mock_session_state, mock_st_write, mock_st_markdown):
        # Prepare a fake selected hike in session_state.
        fake_hike = {'city_name': 'Kathmandu', 'name': 'Everest'}
        mock_session_state['selected_hike'] = fake_hike

        # Return a valid image URL.
        mock_get_trek_image.return_value = "http://example.com/valid_image.jpg"

        module = HikePictureModule()
        module.display()

        # Since the URL is valid, st.markdown should be used to display the image.
        mock_st_markdown.assert_called()
        # st.write should not be called because there is no error.
        mock_st_write.assert_not_called()

    @patch('streamlit.markdown')
    @patch('streamlit.write')
    @patch('streamlit.session_state', new_callable=dict)
    @patch.object(HikePictureModule, 'get_trek_image')
    def test_display_error_image(self, mock_get_trek_image, mock_session_state, mock_st_write, mock_st_markdown):
        # Prepare a fake selected hike.
        fake_hike = {'city_name': 'Kathmandu', 'name': 'Everest'}
        mock_session_state['selected_hike'] = fake_hike

        # Return an error message.
        mock_get_trek_image.return_value = "Error Occurred: API error"

        module = HikePictureModule()
        module.display()

        # When an error occurs, st.write should be called to display the error message.
        mock_st_write.assert_called_with("Error Occurred: API error")
        # st.markdown should not be called in this case.
        mock_st_markdown.assert_not_called()

    # ----- Tests for hike_list_image -----
    @patch('streamlit.markdown')
    @patch.object(HikePictureModule, 'get_trek_image')
    def test_hike_list_image(self, mock_get_trek_image, mock_st_markdown):
        # Simulate get_trek_image returning an error first, then a valid URL.
        mock_get_trek_image.side_effect = [
            "Error Occurred: API error",
            "http://example.com/valid_image.jpg"
        ]

        module = HikePictureModule()
        module.hike_list_image("Everest")

        # Verify that st.markdown was called to display the image.
        mock_st_markdown.assert_called()
        # Ensure get_trek_image was invoked twice.
        self.assertEqual(mock_get_trek_image.call_count, 2)

if __name__ == '__main__':
    unittest.main()
