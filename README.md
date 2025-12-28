Titanic ETL & Data Analysis Project
Project Overview

This project demonstrates an end-to-end ETL (Extract, Transform, Load) pipeline and exploratory data analysis on the Titanic dataset
 using Python, pandas, SQL (SQLite), and data visualization.

The workflow highlights:

Data extraction from CSV

Data cleaning and transformation

Loading into a SQLite database

Running SQL queries to explore and summarize the dataset

Visualizing key insights using matplotlib and seaborn

This project is designed to showcase skills relevant for data analytics and data engineering roles, including Python, SQL, ETL pipelines, and end-to-end project ownership.

Project Structure
mini-etl-titanic/
│
├── data/
│   └── train.csv             # Original Titanic dataset from Kaggle
├── etl-pipeline.py           # ETL and analysis script
├── titanic_cleaned.csv       # Cleaned dataset (generated)
├── titanic.db                # SQLite database (generated)
├── README.md                 # Project documentation
└── venv/                     # Python virtual environment

Getting Started
1. Clone the Repository
git clone <your-repo-url>
cd mini-etl-titanic

2. Create & Activate Virtual Environment
python3 -m venv venv
source venv/bin/activate      # macOS/Linux
# OR
venv\Scripts\activate         # Windows

3. Install Dependencies
pip install pandas sqlalchemy matplotlib seaborn

4. Run the ETL Pipeline
python etl-pipeline.py


This will:

Clean the dataset

Load it into titanic.db

Run SQL queries

Generate visualizations for analysis

Project Highlights
SQL Queries

Survival rate by passenger class

First 10 passengers (data preview)

Survival rate by sex

Visualizations

Bar chart: survival rate by class

Bar chart: survival rate by sex

Histogram: age distribution by survival

Boxplot: fare distribution by class

These plots allow for quick insights into Titanic passenger demographics and survival patterns.

Skills Demonstrated

Python & pandas: Data cleaning, manipulation, transformation

SQL / SQLite: Database creation, querying, aggregation

ETL pipeline: End-to-end data extraction, transformation, and loading

Data visualization: matplotlib & seaborn for storytelling

Portfolio project readiness: GitHub structure, reproducible workflow

Optional Enhancements

Add more advanced queries like GROUP BY Pclass, Sex

Include predictive analysis (logistic regression or classification)

Interactive dashboards using Plotly or Streamlit