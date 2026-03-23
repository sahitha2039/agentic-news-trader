from dotenv import load_dotenv
import os
import requests

load_dotenv()

api_key = os.getenv("NEWS_API_KEY")

url = "https://newsapi.org/v2/everything"
headers = { "X-API-Key": api_key}
params = {
    "q": "stock market OR stocks OR finance OR economy OR earnings OR market OR trading",
    "pageSize": 20,
    "sortBy": "publishedAt"
}
response = requests.get(url, headers=headers, params=params)

if response.status_code == 200:
    data = response.json()
    for i, article in enumerate(data.get("articles", []), start=1):
        print(f"{i}. {article.get('title')} {article.get('source', {}).get('name')} \n")
else:
    print(f"Error: {response.status_code}")