## Functional Specification

## Background  
Finding suitable hikes is challenging due to varying trail conditions, weather, and personal preferences. This tool aims to simplify the search for hikes, assist in training for hiking goals, and help businesses and rangers manage hiking information.  


## User Profile  
### Normal User  
- **Description**: Casual hikers looking for personalized hike recommendations.  
- **Technical Skills**: Can browse the tool.  

### Business User  
- **Description**: Travel agents or guides collecting hike info for clients.  
- **Technical Skills**: Can browse the tool.  

### Ranger  
- **Description**: Trail maintainers checking trail conditions.  
- **Technical Skills**: Can browse the tool.  


## Data Sources  
- **Trail Data**: [WA-RCO Trails Database](https://trails-wa-rco.hub.arcgis.com/datasets/wa-rco::wa-rco-trails-database-public-view/about?layer=0)  
- **Weather Data**: [CoCoRaHS Precipitation Reports](https://www.cocorahs.org/ViewData/ListDailyPrecipReports.aspx)  
- **All Trails Data**: [All Trails Dataset](https://github.com/j-ane/trail-data/blob/master/alltrails-data.csv)  


### User Stories

| Who | Wants | Interaction Methods | Needs | Skills |
|-|-|-|-|-|
| User | Wants to find a hike that aligns with their preferences | Use filters on the tool to provide preferences | Needs the best hike that will align with their preferences | No technical skills |
| User | Wants to find nearby hikes using their location| Provide location to the tool | Needs nearby hikes | No technical skills |  
| User | Wants to see weather report for a hike | Provide hike name | Needs weather report for the hike | No technical skills |  
| User | Wants to see visualization stats for the hike | Provide hike name | Needs visualization stats for the hike | No technical skills |  
| User | Wants to training hiking plan for a given hike | Provide the target hike | Needs training plan | No technical skills | 
| Business User | Wants to collect hike info for their clients | Use filters on the tool to provide preferences | Needs hiking options for their clients | No technical skills |
| Business User | Export CSV of all hikes for clients | Batch export hikes | Needs export to CSV functionality | No technical skills |
| Trail maintainer | Wants to find trails and check trail quality | search for specific trails | Needs comprehensive details on trails | No technical skills | 

### Use Case 1: Find a Hike That Aligns with Preferences  
**Objective of the user interaction:**  
The user wants to find the best hike that matches their specific preferences, such as difficulty level, time of year, and distance.  

**What information does the user provide?**  
- Filters for preferences (e.g., difficulty level, distance, time of year, and weather conditions).  

**What response does the system provide?**  
- A list of hikes that best match the provided preferences, sorted by relevance.  
- Detailed information for each hike, including difficulty level, distance, elevation gain, estimated duration, and user reviews.  

**Steps:**  
1. User navigates to the hike recommendation section of the tool.  
2. User selects filters for preferences, such as difficulty, distance, time of year, and weather conditions.  
3. User submits the selected preferences.  
4. System processes the preferences and searches the hike database.  
5. System generates a list of hikes that best match the provided preferences.  
6. System displays the list of recommended hikes, sorted by relevance.  
7. User selects a hike to view detailed information.  
8. System displays detailed information about the selected hike, including difficulty level, distance, elevation gain, estimated duration, and user reviews.  

**Diagram:**
+-------------------+       +-------------------+       +-------------------+
|      User         |       |        UI         |       | Backend Components|
+-------------------+       +-------------------+       +-------------------+
| Select Filters    | ----> | Filters Display   | ----> | Filter Tool       |
| Enter Trail Name  | ----> | Search Bar        | ----> | Search Tool       |
| Select Hike       | <---- | Hike List Display | <---- | Trail Finder      |
| View Trail Map    | <---- | Trail Map Display | <---- | Trail Database    |
+-------------------+       +-------------------+       +-------------------+
                                                              |
                                                              v
                                                    +-------------------+
                                                    | External Systems  |
                                                    +-------------------+
                                                    | Weather API       |
                                                    +-------------------+



---

### Use Case 2: Get Training Plan for a Specific Hike  
**Objective of the user interaction:**  
The user wants to get a customized training plan to prepare for a specific hike.  

**What information does the user provide?**  
- The target hike they want to train for.  

**What response does the system provide?**  
- A detailed training plan tailored to the selected hike, including recommended exercises, duration, and intensity.  

**Steps:**  
1. User navigates to the training plan section of the tool.  
2. User selects or enters the target hike they want to train for.  
3. User submits the request for a training plan.  
4. System analyzes the difficulty and requirements of the selected hike.  
5. System generates a customized training plan, considering hike difficulty, elevation gain, and distance.  
6. System displays the training plan with recommended exercises, duration, and intensity.  
7. User reviews the training plan and follows it to prepare for the hike.

**Diagram:**
+-------------------+       +-------------------+       +-------------------+
|      User         |       |        UI         |       | Backend Components|
+-------------------+       +-------------------+       +-------------------+
| Select Hike       | ----> | Hike Selection    | ----> | Trail Finder      |
| View Training Plan| <---- | Training Plan    | <---- | Trail Comparison  |
+-------------------+       +-------------------+       +-------------------+
                                                              |
                                                              v
                                                    +-------------------+
                                                    | External Systems  |
                                                    +-------------------+
                                                    | Weather API       |
                                                    +-------------------+



---

### Use Case 3: Export Hike Data to CSV for Business Clients  
**Objective of the user interaction:**  
A business user wants to collect hiking options and export them to a CSV file to share with their clients.  

**What information does the user provide?**  
- Filters to select relevant hikes (e.g., region, difficulty, or popularity).  
- Confirmation for exporting the selected hikes.  

**What response does the system provide?**  
- A downloadable CSV file containing the selected hike data.  

**Steps:**  
1. Business user navigates to the hike collection section of the tool.  
2. Business user applies filters to select relevant hikes for their clients (e.g., region, difficulty, or popularity).  
3. Business user reviews the list of selected hikes.  
4. Business user confirms the export request.  
5. System compiles the hike data based on the selected filters.  
6. System generates a CSV file containing the compiled hike data.  
7. System provides a download link for the CSV file.  
8. Business user downloads the CSV file and shares it with their clients.  

**Diagram:**
+-------------------+       +-------------------+       +-------------------+
|      User         |       |        UI         |       | Backend Components|
+-------------------+       +-------------------+       +-------------------+
| Apply Filters     | ----> | Filters Display   | ----> | Filter Tool       |
| Review Hike List  | <---- | Hike List Display | <---- | Trail Database    |
| Confirm Export    | ----> | Export Confirmation| ---> | Trail Comparison  |
| Download CSV      | <---- | CSV Download Link | <---- | Trail Comparison  |
+-------------------+       +-------------------+       +-------------------+
                                                              |
                                                              v
                                                    +-------------------+
                                                    | External Systems  |
                                                    +-------------------+
                                                    | Weather API       |
                                                    +-------------------+


