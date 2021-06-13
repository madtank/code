This is a sam app using lambda that makes calls to a user api then writes the user data to a dynamodb table. Second function uses dynamodb streams to process the event.

You will first need to create a bucket
aws s3 mb s3://mybucketname

Update the samconfig.toml file and change s3 to your bucket.

you will need sam-cli installed.

easy way is with python3.

pip install aws-sam-cli

sam build
sam deploy

You should be able to invoke your lambda now!