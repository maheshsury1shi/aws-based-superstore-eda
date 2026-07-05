# Project Overview

Exploratory Data Analysis (EDA) on Superstore Sales Data that investigates sales, profit, discount, and quantity across business categories, regions, and customer segments. The project uses Python to clean the dataset, analyze relationships, and produce visualizations for business insights.

# Objectives

- Load and clean the Superstore dataset.
- Analyze sales performance across categories, sub-categories, and regions.
- Identify profit and discount patterns.
- Visualize key relationships and distribution trends.
- Provide a reusable project structure for future analysis.

# Dataset Description

The dataset is stored in Excel format at `data/sample - superstore (2).xlsx`. It includes transaction-level fields such as:

- Order Date, Ship Date
- Category, Sub-Category
- Segment, Region, State
- Sales, Profit, Discount, Quantity

# Folder Structure

```text
cloud-based-superstore-eda/
│
├── README.md
├── LICENSE
├── requirements.txt
├── .gitignore
│
├── data/                 # Source dataset files
├── src/                  # Python scripts and analysis code
├── notebooks/            # Jupyter notebooks for exploration
├── images/               # Output charts and visualizations
├── docs/                 # Project documentation
└── reports/              # Generated reports
```

# Technologies Used

- Python
- pandas
- matplotlib
- seaborn
- openpyxl

# Installation Steps

1. Clone the repository:

```bash
git clone https://github.com/maheshsury1shi/aws-based-superstore-eda.git
cd "Task - 2"
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

# How to Run

From the project root, run the analysis script:

```bash
python src/eda_superstore.py
```

# Visualizations Included

- Category count bar chart
- Sub-category count bar chart
- Segment count bar chart
- Region count bar chart
- State count bar chart
- Sales vs profit scatter plot
- Discount vs profit scatter plot
- Sales histogram
- Profit histogram
- Quantity histogram
- Discount histogram
- Correlation heatmap
- Sales boxplot
- Profit boxplot
- Discount boxplot

# Sample Outputs

Example output files in the `images/` folder:

- `images/category-count.png`
- `images/sales-vs-profit-scatter.png`
- `images/correlation-heatmap.png`
- `images/profit-boxplot.png`

# Future Improvements

- Add time-series sales analysis.
- Build customer segmentation models.
- Create interactive dashboards.
- Add AWS deployment or cloud storage integration.
- Expand reporting with summary dashboards.

