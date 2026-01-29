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




# import asyncio
# from playwright.async_api import async_playwright
# from playwright_stealth import stealth_async
# 
# async def scrape_google(query):
#     async with async_playwright() as p:
#       try:
#         # Launch browser with common anti-detection flags
#         browser = await p.chromium.launch(headless = True)
#         context = await browser.new_context(
#             user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36"
#         )
#         page = await context.new_page()
#         await stealth_async(page)
#         await page.screenshot(path = "debug0.png")
# 
#         # Navigate directly to the search result page
#         url = f"https://www.google.com/search?q={query.replace(' ', '+')}"
#         await page.goto(url)
#         await page.screenshot(path = "debug1.png")
# 
#         # Extract all search result titles and links
#         results = await page.locator(".tF2Cxc").all()
#         for res in results:
#             title = await res.locator("h3").inner_text()
#             link = await res.locator("a").get_attribute("href")
#             print(f"Title: {title}\nLink: {link}\n")
# 
#         await page.screenshot(path = "debug2.png")
#         await browser.close()
#       except Exception as e:
#         print(e)
# 
# try:
#   asyncio.run(scrape_google("2024. évi vállalati pénzügyi adatok és jelentések pdf"))
# except Exception as e:
#   print(e)


