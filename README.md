# 🐦 Bird Monitoring Dashboard

## 📌 Project Overview

The **Bird Monitoring Dashboard** is a data analysis and visualization project developed using Python, Pandas, and Streamlit.

The project analyzes bird observation data collected from two different habitats: **Forest** and **Grassland**. The dashboard provides interactive visualizations and key performance indicators to understand bird species, observations, habitat distribution, and other monitoring patterns.

## 🎯 Problem Statement

Bird monitoring data contains information about bird species, habitats, observation locations, years, sex, distance, and other ecological factors. Analyzing this data manually can be difficult.

The objective of this project is to clean, analyze, and visualize bird monitoring data and provide an interactive dashboard that helps users understand bird observations across Forest and Grassland habitats.

## 🛠️ Technologies Used

* Python
* Pandas
* Streamlit
* Plotly
* Jupyter Notebook
* Microsoft Excel
* Git & GitHub

## 📂 Dataset

The project uses two datasets:

1. **Forest Bird Monitoring Data**
2. **Grassland Bird Monitoring Data**

The datasets contain information such as:

* Administrative Unit
* Site Name
* Plot Name
* Location Type
* Year
* Date
* Observer
* Visit
* Distance
* Sex
* Common Name
* Scientific Name
* Taxon Code
* AOU Code
* Watchlist Status
* Temperature
* Humidity

## 🧹 Data Cleaning

The following data cleaning steps were performed:

* Checked missing values
* Identified duplicate records
* Removed duplicate records
* Handled missing values
* Checked numerical columns
* Combined Forest and Grassland datasets
* Prepared data for analysis and visualization

## 📊 Dashboard Features

### KPI Cards

The dashboard displays:

* **Total Bird Observations**
* **Total Bird Species**
* **Forest Observations**
* **Grassland Observations**

### Interactive Filters

Users can filter the dashboard by:

* Year
* Habitat
* Sex

### Visualizations

The dashboard includes:

1. **Top 10 Bird Species**
2. **Forest vs Grassland Comparison**
3. **Year-wise Bird Observations**
4. **Sex Distribution**
5. **Bird Species by Habitat**
6. **Location Type Analysis**
7. **Observation Distance Distribution**

## 🔄 Project Workflow

```text
Raw Excel Data
      ↓
Data Cleaning
      ↓
Missing Value Handling
      ↓
Duplicate Removal
      ↓
Data Analysis
      ↓
Data Visualization
      ↓
Streamlit Dashboard
      ↓
GitHub
```

## 📁 Project Structure

```text
Bird_Project/
│
├── app.py
├── data_cleaning.ipynb
├── Bird_Monitoring_Data_FOREST.XLSX
├── Bird_Monitoring_Data_GRASSLAND.XLSX
└── README.md
```

## ▶️ How to Run the Project

### 1. Clone the repository

```bash
git clone https://github.com/patilnamu70-droid/Bird-Monitoring-Project.git
```

### 2. Open the project folder

```bash
cd Bird-Monitoring-Project
```

### 3. Install required libraries

```bash
pip install pandas streamlit plotly openpyxl
```

### 4. Run the Streamlit application

```bash
python -m streamlit run app.py
```

The dashboard will open in your web browser.

## 📈 Project Outcome

The project provides an interactive dashboard for analyzing bird monitoring observations across Forest and Grassland habitats.

It helps users:

* Identify commonly observed bird species
* Compare bird observations between habitats
* Analyze yearly observation trends
* Understand bird sex distribution
* Analyze observation locations
* Explore distance-related observations
* Interactively filter monitoring data

## 🚀 Future Improvements

* Add more advanced ecological analysis
* Add geographical/map-based visualization
* Add additional filters
* Add downloadable filtered data
* Deploy the Streamlit dashboard online
* Add advanced statistical analysis

## 👩‍💻 Author

**Namrata Bhaskar Gayakwad**

### Project Type

**Data Analysis & Visualization Project**

### GitHub Repository

https://github.com/patilnamu70-droid/Bird-Monitoring-Project
