This is a sam app using lambda that makes calls to a random jokes api then writes the random joke to a dynamodb table.

You will first need to create a bucket
aws s3 mb s3://mybucketname

Update the samconfig.toml file and change s3 to your bucket.

you will need sam-cli installed.

easy way is with python3.

pip install aws-sam-cli

sam build
sam deploy

You should be able to invoke your lambda now!