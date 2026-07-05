# Project Title

Exploratory Data Analysis (EDA) on Superstore Sales Data

# Project Overview

This project performs exploratory data analysis on Superstore sales data to understand patterns, relationships, and distribution across different business dimensions. The analysis helps in identifying key trends in sales, profit, discount, and quantity using Python and data visualization libraries.

# Objective

The objective of this project is to load the Superstore dataset, clean and prepare it for analysis, and generate meaningful visualizations that support business understanding. The analysis focuses on identifying sales behavior, profit patterns, and potential outliers in the data.

# Dataset

The project uses the Superstore sales dataset provided in Excel format as sample - superstore (2).xlsx. The dataset includes transaction-level information such as order and ship dates, category, sub-category, segment, region, state, sales, profit, discount, and quantity.

# Project Structure

The project consists of a Python script that loads the dataset, performs basic data cleaning, and generates several visualizations to summarize the data.

# Technologies Used

- Python
- Pandas
- Matplotlib
- Seaborn
- OpenPyXL

# Project Workflow

1. Load the dataset from the Excel file.
2. Inspect the structure, columns, and data types.
3. Check for missing values and duplicates.
4. Convert date columns to appropriate datetime format.
5. Generate visualizations for categorical and numerical analysis.
6. Display the results for interpretation.

# Installation

Clone the repository and install the required dependencies:

```bash
pip install -r requirements.txt
```

# How to Run

Run the Python script from the project directory:

```bash
python eda_superstore.py
```

# Visualizations Included

The project contains the following visualizations:

- Bar Charts
- Scatter Plots
- Histograms
- Correlation Heatmap
- Boxplots for Outlier Detection

# Output

The program displays the first rows of the dataset, dataset shape, column names, information about the data, missing values, duplicate count, and a series of visualizations that help interpret relationships and distributions in the sales data.

# Repository Structure

```text
Task -2/
├── .gitignore
├── README.md
├── eda_superstore.py
├── requirements.txt
├── sample - superstore (2).xlsx
└── Task -2.zip
```

# Future Improvements

Additional EDA techniques can be added in the future, such as time-series analysis, customer segmentation, and deeper statistical analysis.

# Author

Mahesh Suryawanshi

