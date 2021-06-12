#/usr/bin/python3
import requests
import json

response = requests.get("https://jsonplaceholder.typicode.com/todos")

# print(response.json())

# print("Data type before reconstruction : ", type(response))

def jprint(obj):
    # create a formatted string of the python json object
    text = json.dumps(obj, sort_keys=true, indent=4)
    print("Data type before reconstruction : ", type(text))

jprint(response.json())