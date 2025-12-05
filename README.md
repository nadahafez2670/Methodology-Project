Amazon Grocery Data Analysis & Classification
📌 Project Overview
Our team collected, cleaned, analyzed, and modeled a real dataset scraped from Amazon Egypt (Grocery Category).
The goal was to practice real-world data handling—from extraction all the way to machine learning modeling and insights generation.

🏗 1. Data Collection

We collected product data using web scraping with Selenium.

🔍 Collected fields:

Product Name

Price

Previous Price

Monthly Purchases

Ratings

Brand (extracted from the first two words of each product name)

🌐 Source:

Amazon Egypt · Grocery Category
150 pages were scraped, and all product details were extracted using Selenium selectors with error-handling for missing values.

🧹 2. Data Inspection

After building the dataset, we inspected it for:

Missing values

Incorrect price formats

Rows with missing product names

Inconsistent rating formats

Text fields requiring extraction or restructuring

The inspection allowed us to identify what needed cleaning and transformation.

🧽 3. Data Cleaning

We applied several cleaning steps, including:

Converting prices into numeric format

Extracting numeric values from monthly purchase strings

Handling missing ratings and pre-prices

Dropping completely empty rows

Ensuring all numeric fields are properly typed

A comparison was made between the raw dataset and the cleaned version.

📊 4. Exploratory Data Analysis (EDA)

We performed an in-depth EDA to understand patterns and relationships in the dataset.

🔎 Included Visualizations:

Distribution of prices

Monthly purchases distribution

Top-selling brands

Correlation heatmaps

Relationship between pricing and sales

Ratings vs Monthly Purchases

The EDA highlighted which brands dominate sales, how prices influence buying behavior, and which features matter most.

🤖 5. Machine Learning Modeling

We trained two classification models to predict whether a product has High Sales (1) or Low Sales (0).
The target variable was created based on the median monthly purchases.

Models Used:

Logistic Regression

Random Forest Classifier

Feature Set:

Price

Ratings

Brand (OneHotEncoded)

📌 Model Performance:
Logistic Regression

Accuracy: 0.63

Performs well on low-sales products but struggles with high-sales prediction.

Random Forest

Accuracy: 0.65

Better balance and stronger performance overall.

Random Forest was the best-performing model in this project.

📁 Deliverables (Matches Project Requirements)

✔ Web scraping script

✔ Raw dataset

✔ Cleaned dataset

✔ Full data inspection summary

✔ EDA visualizations + insights

✔ ML models with evaluation
