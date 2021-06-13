#Lambda reads events from the dynamodb stream#Lambda reads events from the dynamodb stream

import logging
import json
logger = logging.getLogger()
logger.setLevel(logging.INFO)

def lambda_handler(event, context):
  for record in event['Records']:
    if record['eventName'] == 'INSERT':
      newImage = record['dynamodb']['NewImage']
      sendEmailAddress = newImage['email']['S']
      logger.info('Sending email to:' + sendEmailAddress)

    else:
      newImage = record['dynamodb']['NewImage']
      sendEmailAddress = newImage['email']['S']
      logger.info('Not sending email to:' + sendEmailAddress)