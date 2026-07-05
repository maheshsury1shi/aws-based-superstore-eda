# Project Architecture

## Overview

This project follows a simple cloud-enabled analytics architecture:

1. The Superstore dataset is loaded locally from the data folder.
2. Python scripts in the src folder clean and analyze the data.
3. Visualizations and reports are generated into the images and reports folders.
4. The project is deployed on an AWS EC2 Ubuntu instance.
5. Generated artifacts are uploaded to Amazon S3 for storage.
6. CloudWatch Agent collects metrics and logs for monitoring.

## Architecture Diagram

```text
Local Machine
   │
   ▼
Python EDA Script
   │
   ├── Data Cleaning
   ├── Statistical Analysis
   └── Visualization Generation
   │
   ▼
images/ and reports/
   │
   ▼
AWS EC2 Ubuntu Instance
   │
   ├── IAM Role Authentication
   ├── AWS CLI Configuration
   ├── CloudWatch Agent
   └── S3 Upload
   │
   ▼
Amazon S3 + Amazon CloudWatch
```

## Components

- Data Source: Superstore Excel file in the data folder
- Processing Layer: Python with Pandas, NumPy, Matplotlib, and Seaborn
- Output Layer: PNG charts and text/report files
- Cloud Layer: EC2, IAM, S3, CloudWatch
- Monitoring Layer: System metrics and Linux logs

## Deployment Notes

- Use Ubuntu on EC2 for Linux-based monitoring and administration.
- Attach an IAM role to allow access to S3 and CloudWatch.
- Configure the AWS CLI for secure cloud operations.
- Use the CloudWatch Agent to monitor CPU, memory, disk, and log activity.
