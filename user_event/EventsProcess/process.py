#Lambda reads events from the dynamodb stream#Lambda reads events from the dynamodb stream

import os
import logging
import json
import boto3
logger = logging.getLogger()
logger.setLevel(logging.INFO)

def lambda_handler(event, context):
  for record in event['Records']:
    if record['eventName'] == 'INSERT':
      newImage = record['dynamodb']['NewImage']
      sendEmailAddress = newImage['email']['S']
      user_events = get_all_events(sendEmailAddress)
      count_events = str(user_events['Count'])
      logger.info('User had this many other events: ' + count_events)
      logger.info('Sending email to:' + sendEmailAddress)

def get_all_events(sendEmailAddress):
  table_name = os.environ['TABLE_NAME']
# Creating the DynamoDB Client
  dynamodb_client = boto3.client('dynamodb')

  response = dynamodb_client.query(
  TableName=table_name,
  KeyConditionExpression='email = :email',
  ExpressionAttributeValues={":email":{"S":sendEmailAddress}},
  ConsistentRead=True
  )
  return response