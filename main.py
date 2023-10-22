import requests
import json

# Call API endpoint at https://hacker-news.firebaseio.com/v0/ and print the results
response = requests.get("https://hacker-news.firebaseio.com/v0/")
print(response)
