from serpapi import GoogleSearch
import os
from dotenv import load_dotenv
import urllib.request

load_dotenv()

api_key = os.environ['SERPAPI_API_KEY']

for i in range(1): # 3
  params = {
    "engine": "google", # google_images
    "q": "2024. évi vállalati pénzügyi adatok és jelentések pdf",
    "api_key": api_key,
    "gl": "hu",
    "hl": "hu",
    "google_domain": "google.hu", 
    "device": "desktop",
    "num": "10", # 30, 100
    "safe": "off", 
    "start": i * 10 # 0 10 20
  }
  
  search = GoogleSearch(params)
  
  results = search.get_dict()
  
  organic_results = results.get("organic_results", []) 
  
  opener = urllib.request.build_opener()
  opener.addheaders = [('User-Agent', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36')] # ('User-Agent', 'MyApp/1.0')
  urllib.request.install_opener(opener)
  for res in organic_results:
    name = res["title"]
    url = res["link"]
    try:
      urllib.request.urlretrieve(url, f"{name}.pdf")
    except Exception as e:
      print(f"Nem sikerült letölteni: {name} és {url}. A hibaüzenet: {e}")
