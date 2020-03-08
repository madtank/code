
#!python3

import boto3

client = boto3.client('ec2')

response = client.describe_security_groups()

for sg in response['SecurityGroups']:
    print(sg.get("GroupName"))

# print(response['SecurityGroups'])
# print(response)