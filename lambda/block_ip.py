import boto3
import json

def lambda_handler(event, context):
    ip_to_block = event['ip']
    ec2 = boto3.client('ec2')
    response = ec2.revoke_security_group_ingress(
        GroupId='sg-xxxxxxxx',
        IpProtocol='-1',
        CidrIp=f"{ip_to_block}/32"
    )
    return {
        'statusCode': 200,
        'body': json.dumps('IP Blocked')
    }