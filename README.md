# 🌲 LetsGoHike

![Build/Test Workflow](https://github.com/harshilshah4251/LetsGoHike/actions/workflows/build_test.yml/badge.svg)
[![Coverage Status](https://coveralls.io/repos/github/harshilshah4251/LetsGoHike/badge.svg?branch=main)](https://coveralls.io/github/harshilshah4251/LetsGoHike?branch=main)

🚀 **LetsGoHike** is an intelligent hiking companion tool designed to help users discover, plan, and prepare for their next outdoor adventure. The platform offers personalized hiking recommendations, training plans, and hike comparisons based on user preferences and real-time data.

---

## 🛠️ Project Type
- **Tool:** Interactive platform for hike discovery and planning
- **Analysis:** Data-driven insights to help users choose and prepare for hikes effectively

---

## 🛠️ Team Members
- Erin Mee
- Harshil Shah
- Lay Yang
- Rohith C R

---
## ❓ Key Questions of Interest
- 🥾 **Find the Best Hikes:**
    - *"What are the best hikes in my area based on my preferences (elevation, distance, difficulty, weather, season, time of day)?"*
- ⛰️ **Training and Preparation:**
    - *"What types of hikes should I do to prepare for my hiking goal?"*
- 🎒 **Gear Recommendations:**
    - *"What equipment do I need for a particular hike?"*
- 🔍 **Similar Hike Suggestions:**
    - *"Find me a hike similar to one I've done in the past."*

---

## 📂 Folder Structure

```plaintext
LetsGoHike/
├── .github/workflows/            # GitHub Actions CI/CD configuration
│   └── build_test.yml            # Build and test workflow
├── .streamlit/                   # Streamlit configuration
│   └── config.toml               # Streamlit app configuration
├── docs/                         # Documentation and project specifications
│   ├── technology_review/        # Technical review files
│   │   ├── app.py                # Review app script
│   │   ├── technology_review     # Review document
│   │   ├── trails_demo_data.db   # Demo trails database
│   ├── component_specification.md # Component-level details
│   ├── functional_specification.md # Functional requirements
│   └── milestone.md              # Milestone details
├── letsgohike/                   # Core application code
│   ├── __pycache__/              # Python cache
│   ├── LetsGoHike/               # Main app directory
│   ├── modules/                  # Feature modules
│   │   ├── __pycache__/          # Python cache
│   │   ├── __init__.py           # Module initializer
│   │   ├── hike_description_module.py   # Module for hike descriptions
│   │   ├── hike_list_module.py          # Module for hike listings
│   │   ├── hike_map_module.py           # Module for hike map functionality
│   │   ├── hike_picture_module.py       # Module for hike images
│   │   ├── search_module.py             # Module for hike search and filtering
│   │   └── weather_module.py            # Module for weather-related operations
├── tests/                        # Test suite
│   ├── __pycache__/              # Python cache
│   ├── util/                     # Utility tests
│   │   └── __init__.py           # Initialization file for utils
│   ├── __init__.py               # Test suite initialization
│   ├── test_hike_map_module.py   # Tests for hike map functionality
│   ├── test_search_module.py     # Tests for search module
│   └── test_weather_util.py      # Tests for weather utilities

---

## 🎯 Project Goals

### ✅ Core Features
- 🗺️ **Personalized Hike Recommendations:**
    - Suggests hikes tailored to user preferences (distance, difficulty, weather, etc.)
- ⛰️ **Training Plan Generator:**
    - Creates personalized training plans for users preparing to summit specific mountains or achieve hiking goals
- 🥾 **Hike Preparation Guide:**
    - Provides essential details on the equipment and safety tips needed for each hike
- 🔥 **Similar Hike Recommender:**
    - Suggests hikes similar to previous trails based on shared attributes (terrain, elevation, difficulty, etc.)

### 📊 Future Exploratory Features
- 💬 **Community Interaction:**
    - Enable users to connect with other hiking enthusiasts, share tips, and plan group treks
- 📈 **User Activity Visualization:**
    - Interactive visualizations showcasing individual hiking history and progress over time

---

## 📊 Data Sources
The platform uses a combination of real-time and static datasets to provide accurate and personalized hike recommendations.

- 🌿 **Trail Data:**
    - [WA-RCO Trails Database](https://trails-wa-rco.hub.arcgis.com/datasets/wa-rco::wa-rco-trails-database-public-view/about?layer=0) – Comprehensive Washington state trail information
- 🌦️ **Weather Data:**
    - [CoCoRaHS Weather Data](https://www.cocorahs.org/ViewData/ListDailyPrecipReports.aspx) – Daily precipitation reports to assess trail conditions
- 🥾 **Trail Review Data:**
    - [AllTrails Dataset](https://github.com/j-ane/trail-data/blob/master/alltrails-data.csv) – Community-driven hike reviews and information

---

## ⚙️ Technology Stack

- **Frontend:** Streamlit for interactive user interface and data visualization
- **Backend:** Python modules for data filtering, mapping, and recommendation logic
- **Mapping Library:** Folium for rendering trail maps
- **Testing & Coverage:**
    - `unittest` for testing core functionalities
    - `pylint` for static code analysis and linting
    - GitHub Actions for CI/CD workflow with build and test automation
- **Environment:**
    - Virtual environment using `venv`
    - Dependency management with `requirements.txt`

---

## 🚀 Installation & Setup

### 1. Clone the Repository
```bash
git clone https://github.com/harshilshah4251/LetsGoHike.git
cd LetsGoHike

### 2. Create and activate the virtual environment
python3 -m venv letsgohikeenv
source letsgohikeenv/bin/activate  # Mac/Linux
.\letsgohikeenv\Scripts\activate   # Windows

### 3. Install Dependencies
pip install -r requirements.txt

### 4. Run the Application
python -m streamlit run letsgohike/app.py

---

## 📚 Usage Guide

### 1. Search for Hikes:
Input your location, distance, difficulty, and desired weather conditions
The app displays matching hiking trails with a detailed map
### 2. View Hike Details:
Click on a hike to view its details, including distance, elevation gain, and estimated time

---

## 📄 License
This project is licensed under the MIT License – see the LICENSE file for details.
