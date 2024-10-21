# Global Alcohol Consumption Patterns and Health Impacts

## Table of Contents
- Overview and Purpose
- Interactions
- Ethical Considerations
- Data Sources
- Data Dictionary
- Contributors
  
## Overview and purpose
By using the ETL process on the data obtained from Our World in Data, this platform will allow users to explore the demographics of alcohol consumption, trends in consumption over time, and the public health consequences of alcohol use, including addiction and alcohol-related diseases.
This project aims to analyze global alcohol consumption patterns, trends over time, and the associated health impacts. Using data from Our World in Data and the Global Burden of Disease (GBD) Study, we will explore demographics of alcohol consumption, shifts in alcohol use, and public health consequences, such as alcohol-related mortality and diseases.

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
When working on a project related to alcohol consumption patterns and health impacts, several ethical considerations must be taken into account to ensure responsible and respectful handling of the data and its implications. Here are some key ethical aspects to consider:
### 1. Data Privacy and Anonymity
- **Privacy:** Ensure that any data used does not include personally identifiable information (PII) unless you have explicit permission to use it. For example, if the project involves health data from individuals, it's important to anonymize it so that no one can be identified from the dataset.
- **Anonymization:** If any data contains sensitive information (like individual health records), it must be anonymized or aggregated. This ensures that individuals cannot be traced or identified from the data, thus respecting their privacy.
### 2. Data Accuracy and Reliability
- **Accuracy:** Ensure that the data being analyzed is accurate and comes from reliable sources. Misleading or inaccurate data could lead to incorrect conclusions, which can be harmful, especially when it involves health impacts.
- **Source Verification:** Use reputable sources for data collection, such as government health departments, academic institutions, or credible health organizations like the World Health Organization (WHO).
### 3. Data Sensitivity
- **Sensitive Content:** Alcohol consumption and health impacts are sensitive topics. The analysis should be done with caution to avoid stigmatizing or misrepresenting communities, groups, or individuals.
- **Respect for Cultural Differences:** Understand that alcohol consumption is viewed differently across cultures, and ensure that the project does not promote bias or stereotypes.
### 4. Informed Consent
- **Consent:** If the project involves primary data collection (e.g., surveys or interviews), make sure participants provide informed consent. They should be aware of how their data will be used and have the right to withdraw their data if they wish.
- **Transparency:** Be transparent with data subjects about the purpose of the project and how their data will be processed, stored, and shared.
### 5. Non-Stigmatizing Communication
- **Avoid Stigmatization:** Be mindful of the language and visuals used when presenting data. Avoid terms or images that could contribute to the stigma associated with alcohol use or health conditions. Instead, use neutral and respectful language.
- **Consider Context:** Consider the social and cultural contexts when presenting findings. For example, high alcohol consumption rates in certain regions may be linked to socioeconomic factors, which should be addressed with sensitivity.
### 6. Ethical Use of Data Analysis
- **Preventing Harm:** Ensure that your analysis does not lead to harmful consequences, such as promoting irresponsible drinking or enabling discrimination. Be cautious about how findings are interpreted and shared.
- **Avoiding Misinterpretation:** Present data in a way that avoids oversimplification or misleading conclusions. Complex issues, such as the health impacts of alcohol, should be discussed with nuance, considering multiple factors that influence the data.
### 7. Responsible Sharing of Findings
- **Contextualizing Results:** When sharing results, make sure they are presented in context. Highlight potential confounding factors and avoid drawing direct cause-and-effect conclusions unless scientifically supported.
- **Educational Purpose:** Ensure that the project aims to inform and educate rather than to sensationalize or mislead. Emphasize responsible alcohol consumption and awareness of health risks.
### 8. Confidentiality in Data Handling
- **Secure Data Storage:** Use secure methods for storing and processing data, especially if it involves sensitive health information. This includes encryption and access controls to ensure only authorized individuals can access the data.
- **Compliance with Legal Standards:** Adhere to legal frameworks, such as the General Data Protection Regulation (GDPR) or the Health Insurance Portability and Accountability Act (HIPAA), which govern data privacy and security.
### 9. Bias and Ethical AI Considerations
- **Bias in Analysis:** Be aware of potential biases in the data or analysis. For example, datasets may not equally represent all demographics, leading to skewed results. Efforts should be made to acknowledge and mitigate any biases.
- **Algorithmic Transparency:** If machine learning or AI is used for analysis, ensure that the algorithms are transparent and that the decisions they make can be explained and justified.
### 10. Ethical Dissemination
- **Public Communication:** Be careful when disseminating findings to the public or stakeholders. The information should be clear, accurate, and should not promote or encourage harmful behaviors.
- **Ethical Reporting:** Clearly state any limitations of the data or analysis and avoid making unsupported claims. Always cite data sources and provide context for the findings.
### Summary
Ethical considerations are crucial in a project focused on alcohol consumption and health impacts to ensure that:
- Data privacy and confidentiality are respected.
- Findings are accurate, responsible, and culturally sensitive.
- The project promotes awareness and education rather than stigmatization or harm.
By adhering to these ethical guidelines, your project can contribute valuable insights into alcohol consumption patterns while respecting the individuals and communities represented in the data.


## Data Sources
- Our World in Data - Alcohol Consumption Dataset:
Provides comprehensive data on alcohol consumption per capita by type (beer, wine, spirits) and region or country.
  - Our World in Data - Alcohol Consumption
- Global Burden of Disease (GBD) Study:
Contains data on the health impacts of alcohol consumption, including mortality, disease burden, and disability-adjusted life years (DALYs) attributed to alcohol use.

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
