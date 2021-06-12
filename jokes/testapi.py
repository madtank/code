import requests
from pprint import pprint
import boto3
import json

tablename = 'manual input'

response = requests.get('https://official-joke-api.appspot.com/jokes/random')

jokes = json.loads(response.text)

dynamodb = boto3.resource('dynamodb')
id = jokes['id']

table = dynamodb.Table(tablename)
response = table.put_item(
    Item={
        'id': jokes['id'],
        'type': jokes['type'],
        'setup': jokes['setup'],
        'punchline': jokes['punchline']
    }
)




