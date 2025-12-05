## Amazon Grocery Data Analysis & Classification

---

## 📌 Project Overview
This project is part of the **DEPI 2025 final assessment**.  
Our team collected, cleaned, analyzed, and modeled a real dataset scraped from **Amazon Egypt (Grocery Category)**.  
The goal was to practice real-world data handling — from extraction all the way to machine learning modeling and insights generation.

---

## 🏗 1. Data Collection
We collected product data using **web scraping with Selenium**.

### 🔍 Collected Fields:
- Product Name  
- Price  
- Previous Price  
- Monthly Purchases  
- Ratings  
- Brand (extracted from the first two words of each product name)

### 🌐 Source:
- **Amazon Egypt – Grocery Category**  
- **150 pages** were scraped  
- Product details were extracted using **Selenium selectors** with error-handling for missing values

---

## 🧹 2. Data Inspection
After building the dataset, we inspected it for:

- Missing values  
- Incorrect price formats  
- Rows with missing product names  
- Inconsistent rating formats  
- Text fields that required extraction or restructuring  

This inspection helped determine the cleaning and transformation steps needed.

---

## 🧽 3. Data Cleaning
We applied several cleaning operations, including:

- Converting prices into numeric format  
- Extracting numeric values from monthly purchase strings  
- Handling missing ratings and previous prices  
- Dropping completely empty rows  
- Ensuring all numeric fields are correctly typed  

A comparison was made between the **raw dataset** and the **cleaned dataset**.

---

## 📊 4. Exploratory Data Analysis (EDA)
We performed in-depth EDA to understand patterns and relationships within the data.

### 🔎 Included Visualizations:
- Price distribution  
- Monthly purchases distribution  
- Top-selling brands  
- Correlation heatmaps  
- Relationship between pricing and sales  
- Ratings vs Monthly Purchases  

These insights highlighted dominant brands, price influence on sales, and key behavioral patterns.

---

## 🤖 5. Machine Learning Modeling
We trained two classification models to predict whether a product has **High Sales (1)** or **Low Sales (0)**.  
The target variable was created based on the **median monthly purchases**.

### 🧠 Models Used:
- Logistic Regression  
- Random Forest Classifier  

### 🧩 Feature Set:
- Price  
- Ratings  
- Brand (OneHotEncoded)

### 📌 Model Performance:

#### **Logistic Regression**
- **Accuracy:** 0.63  
- Performs well on **low-sales products**  
- Struggles with predicting **high-sales products**

#### **Random Forest**
- **Accuracy:** 0.65  
- More balanced performance overall  
- Best-performing model in this project

---

