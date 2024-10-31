# Global Alcohol Consumption Patterns and Health Impacts

## Table of Contents
- Overview and Purpose
- Interactions
- Ethical Considerations
- Data Sources
- Data Dictionary
- Contributors
  
## Overview and purpose
This project aims to analyze global alcohol consumption patterns, trends over time, and the associated health impacts. By using the ETL process on the data obtained from Our World in Data, this platform will allow users to explore the demographics of alcohol consumption, trends in consumption over time, and the public health consequences of alcohol use, including addiction and alcohol-related diseases.
Using data from Our World in Data and the Global Burden of Disease (GBD) Study, we will explore demographics of alcohol consumption, shifts in alcohol use, and public health consequences, such as alcohol-related mortality and diseases.

## Interactions
### Flask Deployment Guide
**Step 1:** Clone the Repository  
git clone https://github.com/hopkinsbowman78/Global_Alcohol_Consumption_Patterns_and_Health_Impacts.git

**Step 2:** Navigate to the Project Directory

**Step 3:** Create a Virtual Environment (Recommended)  
**On Windows:**  python -m venv venv  
**On macOS/Linux:**  source venv/bin/activate  

**Step 4:** Install Dependencies  
pip install -r requirements.txt

**Step 5:** Run the Flask App  
python app.py

**Step 6:** Your Flask should be running locally.  
Access it by navigating to: http://127.0.0.1:5000


## Ethical Considerations
Ethical considerations are essential in projects on alcohol consumption patterns and health impacts to ensure respectful, responsible handling of data. Key aspects include maintaining data privacy through anonymization and consent, ensuring accuracy by sourcing reliable data, and being sensitive to cultural perspectives to avoid stigma. Transparent communication about data usage, secure data storage, and compliance with legal standards like GDPR are critical for confidentiality. Findings should aim to educate without bias or sensationalism, considering the social context to prevent misinterpretation. Adhering to these guidelines allows the project to inform responsibly while respecting individuals and communities.


## Data Sources
- Our World in Data - Alcohol Consumption Dataset:
Provides comprehensive data on alcohol consumption per capita by type (beer, wine, spirits) and region or country.
  - [Our World in Data - Alcohol Consumption](https://ourworldindata.org/alcohol-consumption)
- Global Burden of Disease (GBD) Study:
Contains data on the health impacts of alcohol consumption, including mortality, disease burden, and disability-adjusted life years (DALYs) attributed to alcohol use.
  - [Global Burden of Disease (GBD) Study](https://www.healthdata.org/research-analysis/gbd-data)

## Data Dictionary

This table provides detailed descriptions of each column in the dataset used for the Global Alcohol Consumption project.

| Column Name                     | Description                                                                                                             |
|---------------------------------|-------------------------------------------------------------------------------------------------------------------------|
| `entity`                        | The name of the country or region.                                                                                      |
| `year`                          | The year the data was recorded.                                                                                         |
| `alcohol_consumption_per_capita`| Total alcohol consumption per capita (liters of pure alcohol, projected estimates, 15+ years of age).                   |
| `gdp_per_capita`                | GDP per capita, PPP (constant 2017 international $).                                                                    |
| `alcohol_related_mortality`     | Alcohol-attributable fractions, all-cause deaths (%) - Sex: both sexes.                                                |



## Contributors
- Amie Mccall
- Heather Bowman
- Khalia Boone
- Jazmin Austin
