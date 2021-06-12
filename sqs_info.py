import boto3
import json

client = boto3.client('sqs',region_name='us-east-2')


q_urls = client.list_queues()

if 'QueueUrls' in q_urls:
  for QueueUrl in q_urls['QueueUrls']:
    print(QueueUrl)
    q_attributes = client.get_queue_attributes(
    QueueUrl=QueueUrl,
    AttributeNames=[
      'Policy',
    ]
    )


    print(q_attributes)
    y = json.loads(q_attributes['Attributes']['Policy'])
    for x in y['Statement']:
      print(x)
    

'''working code
    y = json.loads(q_attributes['Attributes']['Policy'])
    for attr, rule in y['Statement'][0].items():
      print(str(attr) + ',' + str(rule))
    '''
