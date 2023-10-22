import requests
import json

# Call API endpoint at https://hacker-news.firebaseio.com/v0/ and print the results
response = requests.get("https://hacker-news.firebaseio.com/v0/item/37958765.json?print=pretty")
data = response.text
parse_json = json.loads(data)

print(parse_json['time'])