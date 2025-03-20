import pytest
import streamlit as st
import google.generativeai as genai
 
from letsgohike.modules.hike_plan_module import HikePlanModule

# Dummy response class to simulate a valid API response.
class DummyResponse:
    def __init__(self, text):
        self.text = text

# Dummy model that returns a valid response.
class DummyModel:
    def __init__(self, model_name):
        self.model_name = model_name

    def generate_content(self, prompt):
        return DummyResponse("Test trek plan text.")

# Dummy model that simulates an API error by raising an exception.
class DummyModelError:
    def __init__(self, model_name):
        self.model_name = model_name

    def generate_content(self, prompt):
        raise Exception("API error")

# Test for a successful API call in get_trek_plan.
def test_get_trek_plan_success(monkeypatch):
    # Patch the genai functions.
    monkeypatch.setattr(genai, "configure", lambda api_key: None)
    monkeypatch.setattr(genai, "GenerativeModel", lambda model_name: DummyModel(model_name))
    
    module = HikePlanModule()
    result = module.get_trek_plan("Test Trek", "dummy_api_key")
    assert result == "Test trek plan text."

# Test for get_trek_plan when an exception occurs.
def test_get_trek_plan_error(monkeypatch):
    monkeypatch.setattr(genai, "configure", lambda api_key: None)
    monkeypatch.setattr(genai, "GenerativeModel", lambda model_name: DummyModelError(model_name))
    
    module = HikePlanModule()
    result = module.get_trek_plan("Test Trek", "dummy_api_key")
    assert "Issues with genai: API error" in result

# Test the display function when a valid 'selected_hike' exists in session_state.
def test_display_valid(monkeypatch):
    # Set a dummy hike in the session_state.
    st.session_state["selected_hike"] = {"name": "Test Trek", "city_name": "Test City"}
    
    # Create an instance of the module and patch get_trek_plan to return a test string.
    module = HikePlanModule()
    monkeypatch.setattr(module, "get_trek_plan", lambda trek_name, api_key: "Test trek plan text.")
    
    # Capture outputs from st.markdown and st.write.
    markdown_outputs = []
    write_outputs = []
    monkeypatch.setattr(st, "markdown", lambda text, unsafe_allow_html=False: markdown_outputs.append(text))
    monkeypatch.setattr(st, "write", lambda text: write_outputs.append(text))
    
    module.display()
    
    # Check that the markdown header is correctly formatted.
    expected_header = "<p style='color:#e0f0d8; font-weight:bold;'>Trek Plan for Test Trek,Test City </p>"
    assert expected_header in markdown_outputs
    # Check that the description from get_trek_plan is written.
    assert "Test trek plan text." in write_outputs

# Test the display function when there is no selected_hike.
def test_display_no_selected_hike(monkeypatch):
    # Ensure selected_hike is not in session_state.
    if "selected_hike" in st.session_state:
        del st.session_state["selected_hike"]
    
    write_outputs = []
    monkeypatch.setattr(st, "write", lambda text: write_outputs.append(text))
    monkeypatch.setattr(st, "markdown", lambda text, unsafe_allow_html=False: None)
    
    module = HikePlanModule()
    module.display()
    
    # When no selected_hike is set, nothing should be written.
    assert write_outputs == []
