import json
import boto3

client = boto3.client('iam')
response = client.get_account_password_policy(
)

# for key, value in response['PasswordPolicy'].items():
#   print(key, value)

account = '123456'
for attr, rule in response['PasswordPolicy'].items():
  # print('For rule ' + attr + ' ' + 'is set to ' + rule)
  print(str(account) + ',' + str(attr) + ',' + str(rule))


