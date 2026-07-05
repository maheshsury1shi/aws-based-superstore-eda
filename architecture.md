# Project Architecture

## Overview

This project follows a simple cloud-enabled analytics architecture where the Superstore dataset is analyzed with Python and the generated outputs are stored and monitored on AWS.

## Architecture Diagram

```text
Superstore Dataset (.xlsx)
          │
          ▼
Python EDA Application
(Pandas, NumPy, Matplotlib, Seaborn)
          │
          ▼
Ubuntu EC2 Instance
          │
          ▼
Generate Charts & Reports
          │
          ├──────────────► Amazon S3
          │                 (Store Charts & Reports)
          │
          ▼
CloudWatch Agent
          │
          ├──────────────► CloudWatch Metrics
          │
          └──────────────► CloudWatch Logs
```

This architecture shows how the Superstore dataset is analyzed locally using Python, the generated charts and reports are produced on an Ubuntu EC2 instance, and the results are stored in Amazon S3 while system health is monitored through CloudWatch Metrics and CloudWatch Logs.

## Flow Explanation

1. The Superstore dataset is loaded into a Python EDA application.
2. The application analyzes the data using Pandas, NumPy, Matplotlib, and Seaborn.
3. Charts and reports are generated on the Ubuntu EC2 instance.
4. The outputs are uploaded to Amazon S3 for storage.
5. The CloudWatch Agent collects metrics and logs from the EC2 instance.
6. Monitoring data is sent to CloudWatch Metrics and CloudWatch Logs.

## Project Workflow

```text
                  +---------------------------+
                  |   Superstore Dataset      |
                  |     (.xlsx File)          |
                  +------------+--------------+
                               |
                               v
                  +---------------------------+
                  | Python EDA Application    |
                  | Pandas • NumPy            |
                  | Matplotlib • Seaborn      |
                  +------------+--------------+
                               |
                               v
                  +---------------------------+
                  | Data Processing           |
                  | • Data Cleaning           |
                  | • Missing Value Analysis  |
                  | • Duplicate Detection     |
                  | • Statistical Summary     |
                  +------------+--------------+
                               |
                               v
                  +---------------------------+
                  | Exploratory Data Analysis |
                  | • Histograms              |
                  | • Boxplots                |
                  | • Heatmap                 |
                  | • Scatter Plots           |
                  | • Category Analysis       |
                  | • Sales & Profit Analysis |
                  +------------+--------------+
                               |
                               v
                  +---------------------------+
                  | Generate Output           |
                  | • Charts (.png)           |
                  | • Reports (.txt/.md)      |
                  +------------+--------------+
                               |
                               v
        +----------------------------------------------+
        | Deploy & Execute on AWS EC2 (Ubuntu Linux)   |
        +----------------------+-----------------------+
                               |
                               v
                  +---------------------------+
                  | Python Virtual Environment|
                  | Install Dependencies      |
                  | Run EDA Script            |
                  +------------+--------------+
                               |
                  +------------+------------+
                  |                         |
                  v                         v
      +----------------------+   +----------------------+
      | Amazon S3            |   | CloudWatch Agent     |
      | Store Charts         |   | Collect Metrics      |
      | Store Reports        |   | Collect Logs         |
      +----------+-----------+   +----------+-----------+
                 |                          |
                 |                          |
                 v                          v
      +----------------------+   +----------------------+
      | S3 Bucket            |   | Amazon CloudWatch    |
      | Project Artifacts    |   | Metrics & Logs       |
      +----------------------+   +----------------------+
```

This workflow begins with the Superstore dataset and moves through data processing, exploratory analysis, and output generation. Once the charts and reports are created, the project is deployed on an Ubuntu EC2 instance, where the Python environment is set up, the EDA script is executed, and the results are stored in Amazon S3. At the same time, the CloudWatch Agent collects performance metrics and logs, which are monitored in Amazon CloudWatch.

## Components

- Data Source: Superstore Excel file in the data folder
- Processing Layer: Python with Pandas, NumPy, Matplotlib, and Seaborn
- Output Layer: PNG charts and report files
- Cloud Layer: EC2, Amazon S3, and CloudWatch
- Monitoring Layer: System metrics and Linux logs

## Deployment Notes

- Use Ubuntu on EC2 for Linux-based monitoring and administration.
- Configure the AWS CLI and required permissions for S3 and CloudWatch.
- Use the CloudWatch Agent to monitor CPU, memory, disk, and log activity.
