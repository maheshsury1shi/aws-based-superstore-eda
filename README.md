# 🚀 AWS-Based Superstore EDA

![Python](https://img.shields.io/badge/Python-3.10%2B-3776AB?logo=python&logoColor=white) ![AWS EC2](https://img.shields.io/badge/AWS-EC2-FF9900?logo=amazonaws&logoColor=white) ![CloudWatch](https://img.shields.io/badge/AWS-CloudWatch-FF4F8B?logo=amazoncloudwatch&logoColor=white) ![Amazon S3](https://img.shields.io/badge/AWS-S3-569A31?logo=amazons3&logoColor=white) ![Linux](https://img.shields.io/badge/Linux-Ubuntu-E95420?logo=ubuntu&logoColor=white) ![Pandas](https://img.shields.io/badge/Pandas-2.x-150458?logo=pandas&logoColor=white) ![NumPy](https://img.shields.io/badge/NumPy-2.x-013243?logo=numpy&logoColor=white) ![Matplotlib](https://img.shields.io/badge/Matplotlib-3.x-11557C?logo=matplotlib&logoColor=white) ![Seaborn](https://img.shields.io/badge/Seaborn-0.x-4C72B0?logo=python&logoColor=white) ![GitHub](https://img.shields.io/badge/GitHub-Repository-181717?logo=github&logoColor=white)

> A cloud-focused Exploratory Data Analysis project that transforms the Superstore dataset into actionable business insights while demonstrating AWS deployment, Linux administration, and system monitoring skills.

## Project Banner

# 📊 Superstore Insights with AWS & Linux

> From local Python analysis to cloud-based monitoring and reporting on Amazon Web Services.

## Project Description

This repository showcases an end-to-end analytics workflow for the Superstore dataset using Python, Pandas, Matplotlib, and Seaborn. The project goes beyond traditional data analysis by demonstrating how analytical outputs can be deployed and monitored in a real AWS environment. It highlights both Data Analytics and Cloud Engineering capabilities for modern engineering and business intelligence workflows.

## Key Features

- 📊 Data cleaning, validation, and missing value analysis
- 🔍 Descriptive statistics and correlation analysis
- 📈 Histogram, boxplot, scatter plot, and heatmap generation
- 🧠 Category, region, segment, and state-level business insights
- ☁️ AWS EC2 deployment and monitoring setup
- 📦 S3-based storage for reports and visualizations
- 🐧 Linux administration and CloudWatch integration

## AWS Services Used

- Amazon EC2: Hosts the Python environment on an Ubuntu Linux instance for deployment and remote operations.
- IAM Roles: Provides secure, role-based access to AWS services without hardcoded credentials.
- Amazon S3: Stores generated reports, charts, and project artifacts.
- Amazon CloudWatch: Monitors system performance, logs, and operational health.
- CloudWatch Agent: Collects system metrics and logs from the Linux server.
- AWS CLI: Enables command-line interaction for configuration and cloud resource management.

## Linux Skills Demonstrated

- SSH access to an EC2 instance
- Linux file and directory management
- Package installation and system updates
- Python virtual environment setup
- Monitoring CPU, memory, disk, and network usage
- Log review and system troubleshooting
- AWS CLI and CloudWatch agent configuration

## Project Architecture

The architecture for this project is documented in [architecture.md](architecture.md).

## Workflow

1. Load and clean the Superstore dataset locally using Python.
2. Generate analytical reports and visualizations with Pandas, Matplotlib, and Seaborn.
3. Save outputs to the local repository under the images and reports folders.
4. Deploy the project environment on an AWS EC2 Ubuntu instance.
5. Configure IAM roles, AWS CLI, and required packages.
6. Upload generated artifacts to Amazon S3.
7. Install and configure the CloudWatch Agent to collect metrics and logs.
8. Monitor system health and operational performance in CloudWatch.

## Technology Stack

| Category | Tools |
| --- | --- |
| Programming | Python |
| Data Analysis | Pandas, NumPy |
| Visualization | Matplotlib, Seaborn |
| Cloud Platform | AWS EC2, S3, CloudWatch, IAM |
| Operating System | Linux (Ubuntu) |
| Version Control | Git, GitHub |

## Folder Structure

```text
aws-based-superstore-eda/
├── aws-console-&-linux/   # AWS and Linux screenshots
├── data/                  # Source dataset files
├── docs/                  # Documentation and screenshots
├── images/                # Generated visualizations
├── reports/               # CSV/text reports and outputs
├── src/                   # Python analysis scripts
├── LICENSE
├── README.md
├── architecture.md
├── requirements.txt
└── .gitignore
```

## Installation

```bash
git clone https://github.com/maheshsury1shi/aws-based-superstore-eda.git
cd aws-based-superstore-eda
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## Running the Project

```bash
python src/eda_superstore.py
```

This will generate charts in the images folder and reports in the reports folder.

## AWS Deployment Steps

### 1. EC2
- Launch an Ubuntu EC2 instance in the desired AWS region.

### 2. IAM Role
- Attach an IAM role with permissions for S3 and CloudWatch access.

### 3. Python Virtual Environment
- Create and activate a Python virtual environment on the EC2 instance.

### 4. AWS CLI
- Configure AWS CLI with your credentials and default region.

### 5. S3 Upload
- Upload generated reports and images to an S3 bucket.

### 6. CloudWatch Agent
- Install and configure the CloudWatch Agent on the Linux server.

### 7. CloudWatch Logs
- Enable log collection for system and application logs.

### 8. CloudWatch Metrics
- Monitor CPU, memory, disk usage, and network performance.

## Project Screenshots

- docs/ec2-instance.png
- docs/cloudwatch-dashboard.png
- docs/cloudwatch-logs.png
- docs/s3-bucket.png
- docs/aws-architecture.png
- docs/linux-terminal.png
- docs/project-output.png

Example screenshots from the AWS and Linux workflow are available in [aws-console-&-linux](aws-console-&-linux).

## Generated Visualizations

- [images/category-count.png](images/category-count.png)
- [images/sub-category-count.png](images/sub-category-count.png)
- [images/segment-count.png](images/segment-count.png)
- [images/region-count.png](images/region-count.png)
- [images/state-count.png](images/state-count.png)
- [images/sales-vs-profit-scatter.png](images/sales-vs-profit-scatter.png)
- [images/discount-vs-profit-scatter.png](images/discount-vs-profit-scatter.png)
- [images/sales-histogram.png](images/sales-histogram.png)
- [images/profit-histogram.png](images/profit-histogram.png)
- [images/quantity-histogram.png](images/quantity-histogram.png)
- [images/discount-histogram.png](images/discount-histogram.png)
- [images/correlation-heatmap.png](images/correlation-heatmap.png)
- [images/sales-boxplot.png](images/sales-boxplot.png)
- [images/profit-boxplot.png](images/profit-boxplot.png)
- [images/discount-boxplot.png](images/discount-boxplot.png)

## Learning Outcomes

- Stronger understanding of AWS cloud services and infrastructure monitoring
- Practical Linux administration and remote server management experience
- Improved Python-based data analysis and visualization skills
- Hands-on exposure to logging, metrics, and operational observability
- Confidence in building end-to-end analytics projects for real-world use cases

## Future Enhancements

- Streamlit dashboard for interactive exploration
- Docker containerization for portability
- Terraform-based infrastructure automation
- AWS Lambda-based automation workflows
- Amazon QuickSight integration for business dashboards
- CI/CD pipelines using GitHub Actions

## Author

Mahesh Suryawanshi

## Connect With Me

- GitHub: https://github.com/maheshsury1shi
- LinkedIn: https://www.linkedin.com/in/maheshsury1shi/
- Email: maheshsury1shi@gmail.com

## License

This project is licensed under the MIT License. See [LICENSE](LICENSE) for details.

