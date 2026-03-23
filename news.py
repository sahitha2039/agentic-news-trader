from dotenv import load_dotenv
import os
import requests

load_dotenv()

api_key = os.getenv("NEWS_API_KEY")

url = "https://newsapi.org/v2/everything"
headers = { "X-API-Key": api_key}
params = {
    "q": "stock market", 
}
response = requests.get(url, headers=headers, params=params)

if response.status_code == 200:
    data = response.json()
    print(data)
else:
    print(f"Error: {response.status_code}")