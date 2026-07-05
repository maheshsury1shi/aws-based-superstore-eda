# Exploratory Data Analysis (EDA)
# Superstore Sales Dataset

# Import Libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 1. Data Loading

# Load Dataset
df = pd.read_excel("sample - superstore (2).xlsx")

# Display First 10 Rows
print("First 10 Rows:")
print(df.head(10))

# Display Shape
print("\nShape of Dataset:")
print(df.shape)

# Display Column Names
print("\nColumn Names:")
print(df.columns)

# Display Basic Information
print("\nDataset Information:")
print(df.info())

# 2. Data Cleaning

# Check Missing Values
print("\nMissing Values:")
print(df.isnull().sum())

# Handle Missing Values (Optional)
df = df.dropna()

# Check Data Types
print("\nData Types:")
print(df.dtypes)

# Convert Data Types if Necessary
df['Order Date'] = pd.to_datetime(df['Order Date'])
df['Ship Date'] = pd.to_datetime(df['Ship Date'])

# Check for Duplicates
print("\nDuplicate Rows:")
print(df.duplicated().sum())

# 3. Visualization

sns.set(style="whitegrid")

# ---------- Bar Chart : Category ----------
plt.figure(figsize=(8,5))
sns.countplot(x='Category', data=df)
plt.title("Category")
plt.xticks(rotation=45)
plt.show()

# ---------- Bar Chart : Sub-Category ----------
plt.figure(figsize=(12,6))
sns.countplot(x='Sub-Category', data=df)
plt.title("Sub-Category")
plt.xticks(rotation=90)
plt.show()

# ---------- Bar Chart : Segment ----------
plt.figure(figsize=(8,5))
sns.countplot(x='Segment', data=df)
plt.title("Segment")
plt.show()

# ---------- Bar Chart : Region ----------
plt.figure(figsize=(8,5))
sns.countplot(x='Region', data=df)
plt.title("Region")
plt.show()

# ---------- Bar Chart : State ----------
plt.figure(figsize=(15,6))
sns.countplot(y='State', data=df, order=df['State'].value_counts().index)
plt.title("State")
plt.show()

# ---------- Scatter Plot : Sales vs Profit ----------
plt.figure(figsize=(8,5))
sns.scatterplot(x='Sales', y='Profit', data=df)
plt.title("Sales vs Profit")
plt.show()

# ---------- Scatter Plot : Discount vs Profit ----------
plt.figure(figsize=(8,5))
sns.scatterplot(x='Discount', y='Profit', data=df)
plt.title("Discount vs Profit")
plt.show()

# ---------- Histogram : Sales ----------
plt.figure(figsize=(8,5))
plt.hist(df['Sales'], bins=30)
plt.title("Sales")
plt.xlabel("Sales")
plt.ylabel("Frequency")
plt.show()

# ---------- Histogram : Profit ----------
plt.figure(figsize=(8,5))
plt.hist(df['Profit'], bins=30)
plt.title("Profit")
plt.xlabel("Profit")
plt.ylabel("Frequency")
plt.show()

# ---------- Histogram : Quantity ----------
plt.figure(figsize=(8,5))
plt.hist(df['Quantity'], bins=30)
plt.title("Quantity")
plt.xlabel("Quantity")
plt.ylabel("Frequency")
plt.show()

# ---------- Histogram : Discount ----------
plt.figure(figsize=(8,5))
plt.hist(df['Discount'], bins=30)
plt.title("Discount")
plt.xlabel("Discount")
plt.ylabel("Frequency")
plt.show()

# ---------- Heatmap ----------
plt.figure(figsize=(6,5))

corr = df[['Sales', 'Profit', 'Discount', 'Quantity']].corr()

sns.heatmap(corr,
            annot=True,
            cmap='coolwarm')

plt.title("Correlation Heatmap")
plt.show()

# 4. Outlier Detection

# Boxplot : Sales
plt.figure(figsize=(8,5))
sns.boxplot(x=df['Sales'])
plt.title("Sales")
plt.show()

# Boxplot : Profit
plt.figure(figsize=(8,5))
sns.boxplot(x=df['Profit'])
plt.title("Profit")
plt.show()

# Boxplot : Discount
plt.figure(figsize=(8,5))
sns.boxplot(x=df['Discount'])
plt.title("Discount")
plt.show()