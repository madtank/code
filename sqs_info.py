import boto3

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
    
    
    print(q_attributes['Attributes']['Policy'])


