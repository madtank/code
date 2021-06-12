import os
import boto3
import requests
import logging
import json
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

ddbtable = os.environ['TABLE_NAME']
apiurl = os.environ['apiurl']


def lambda_handler(event, context):
  response = requests.get(apiurl)
  logger.info(response)
  jokes = json.loads(response.text)
  update_ddb(jokes)

def update_ddb(jokes):
  dynamodb = boto3.resource('dynamodb')
  table = dynamodb.Table(ddbtable)
  response = table.put_item(
      Item={
          'id': jokes['id'],
          'type': jokes['type'],
          'setup': jokes['setup'],
          'punchline': jokes['punchline']
      }
  )
  logger.info(response)
