#This lambda function gets the data from api and writes to a database

import os
import boto3
import requests
import logging
import json
logger = logging.getLogger()
logger.setLevel(logging.INFO)


ddbtable = os.environ['TABLE_NAME']
apiurl = os.environ['apiurl']

#Make an api call to get the data we want
def lambda_handler(event, context):
  campaign_name = event['campaign_name']
  response = requests.get(apiurl)
  response_data = json.loads(response.text)
  user_events = response_data['data']
  updatedb(user_events,campaign_name)

#Add the data to the datbase
def updatedb(user_events,campaign_name):
  dynamodb = boto3.resource('dynamodb')
  table = dynamodb.Table(ddbtable)
  for user_event in user_events:
    email = user_event['email']
    # id = campaign_name + '-' + email
    response = table.put_item(
      Item={
          'email': user_event['email'],
          'campaign_name': campaign_name,
          'first_name': user_event['first_name'],
          'last_name': user_event['last_name']
      }
    )