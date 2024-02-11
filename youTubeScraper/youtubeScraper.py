import requests
import json
from bs4 import BeautifulSoup

def search_youtube(query, max_results=40):
    base_url = "https://www.youtube.com/results"
    params = {
        "search_query": query,
        "sp": "EgIQAQ%253D%253D",  # Filter for Creative Commons videos
    }

    response = requests.get(base_url, params=params)
    soup = BeautifulSoup(response.content, "html.parser")
    all_divs = soup.find_all("div", id="primary")
    print(all_divs)


search_youtube("Humans")