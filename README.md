# Spring 2019 IEOR 135/290 Group9: Employment Dynamics
Team Members: Rohit Govindan, Lih Yun Chang, Lu Wang, Ziyu Li, Ran Meng

Project Industry Mentor: James Hodson (AI4Good)
####![alt text](https://github.com/rohigovi/EmploymentDynamics/blob/master/Bay%20Area.PNG)

## Description:
In this project, we have used machine learning tools to delve into the different factors affecting an employee's vulnerability to layoffs across 5 major industries in the Bay Area.\
\
*The main datasets we use are:*\
**The Bay Area Employee Dataset:**\
This dataset(containing over 23 million rows!) has been scraped from resumes of employees in Bay Area and provided by our mentor.
It contains 21 employee features. Important Features include: Gender, Self reported primary and secondary skillsets and their corresponding weights, city, country, company name, start date of employment.\

**The Bay Area WARN Dataset:**\
The Worker Adjustment and Retraining Notification(WARN) Act protects employees by requiring most employers with 100 or more employees to provide advance notification of plant closings and mass layoffs of employees.\

We use this dataset to tell when major layoffs occur, and how many people are affected(between 2014-2018).\

**Please visit our website(Especially the Data Analysis and Employee Guide Section) to see our final deliverable: https://ieor135project.wixsite.com/website\**

**You can also visit this link to view our research report: https://docs.google.com/document/d/1S-92MxKjig6cGqKBzO2M7Bqr5xPFw4AzbUH2oFTamV0/edit?usp=sharing\**
\
This repoistory is used to keep all relevant code and literature for IEOR 135/290 group 9's project: Employment Dynamics. The project is supervised by James Hodson, director of AI4good foundation.\

## File structure:

The repository contains 6 subdirectories, namely *ImportantCSVs*, *Models* and *Pre- processing*, *Python Notebooks for Visiualizations*, *Reports and Miscellaneous* and **Visualization**:

+ **Pre- Processing**: Contains code to combine the bayarea dataset provided by mentor and the WARN notices, and cleaning the combined dataset with string manipulation, logical subsetting etc, before the dataset is ready for ML training

+ **ImportantCSVs**: Contains all datasets we worked with for prescriptive modeling. 

+ **Models**: Contains all ML models we implemented throughout the semester, including but not limited to preditions of layoff profiles and extracting the driving factors behind layoff events  .  

+ **Python Notebooks for Visiualizations**:  Contains all code to generate EDAs, descriptive modelling and time-series analysis

+ **Reports and Miscellaneous**: Contains the initial exploration reports drafted during the beginning of semester for documenting the reserach progress

+ **Visiualization**: Contains Tableau visiualization that summarizes our findings by the low-tech demo date 


We also published summary of our analysis & findings on [website](https://ieor135project.wixsite.com/website) as the UI for the project. 

