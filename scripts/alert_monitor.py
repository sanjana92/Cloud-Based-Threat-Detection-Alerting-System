import re
import boto3

sns = boto3.client('sns')
TOPIC_ARN = 'arn:aws:sns:us-west-2:111111111111:ctdas-alerts'

def detect_brute_force(log_file):
    with open(log_file) as f:
        content = f.readlines()

    failed_attempts = {}
    for line in content:
        if "Failed password" in line:
            ip = re.findall(r'from (\d+\.\d+\.\d+\.\d+)', line)
            if ip:
                ip = ip[0]
                failed_attempts[ip] = failed_attempts.get(ip, 0) + 1

    for ip, count in failed_attempts.items():
        if count >= 5:
            sns.publish(Subject="Brute Force Detected",
                        Message=f"{ip} attempted {count} logins",
                        TopicArn=TOPIC_ARN)

detect_brute_force("/var/log/auth.log")