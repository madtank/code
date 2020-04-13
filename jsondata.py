import json
import boto3
from botocore.exceptions import ClientError

client = boto3.client('iam')
account = '123456'



try:
  response = client.get_account_password_policy()
  for attr, rule in response['PasswordPolicy'].items():
    # print('For rule ' + attr + ' ' + 'is set to ' + rule)
    print(str(account) + ',' + str(attr) + ',' + str(rule))
except ClientError as e1:
  if e1.response["Error"]["Code"] == "NoSuchEntity":
    response = client.update_account_password_policy(
      MinimumPasswordLength=8,
      RequireNumbers=True,
    )
  print(response)
