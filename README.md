# Cloud-based Threat Detection & Alerting System (CTDAS)

![CTDAS Architecture](assets/ctdas-architecture.png)



This project simulates a real-world security detection and alerting system using AWS and Wazuh.

## Features
- Detect brute force attacks on EC2 SSH
- Send real-time alerts via AWS SNS
- Optional auto-blocking via Lambda
- Infrastructure as Code with Terraform

## Setup
1. Deploy EC2 and S3 with Terraform
2. Install Apache & Wazuh on EC2
3. Configure CloudWatch and cron for monitoring
4. Set up Lambda for response
5. Connect alerts to SNS topic

## Tools Used
- AWS (EC2, S3, Lambda, SNS)
- Terraform
- Python
- Wazuh
- Apache
