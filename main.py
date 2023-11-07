from bs4 import BeautifulSoup
import requests
import pprint
from datetime import datetime

website_count = dict()
today_date = "2023-10-29"
BASE_URL = "https://news.ycombinator.com/"
query_url = BASE_URL + "front?day=" + today_date

today_posts = requests.get(query_url)
soup = BeautifulSoup(today_posts.content, "html.parser")
post_elements = soup.find_all("tr", class_="athing")

for post in post_elements:
    website_element= post.find("span", class_="sitestr")
    if website_element:
        website_name = website_element.text
        website_count[website_name] = website_count.get(website_name, 0) + 1    

pprint.pprint(website_count)