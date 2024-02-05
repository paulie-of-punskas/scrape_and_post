# === scrape websites and extract specific information
import requests
from bs4 import BeautifulSoup
from datetime import datetime

# ==== check if URLs respond 200
url = ["https://www.adidas.ch/de/future-icons-3-streifen-woven-hose/HK2142.html",
       "https://www.adidas.ch/de/adicolor-classics_-sst-trainingshose/IJ6998.html"]

user_agent_desktop = 'Safari/537.36'

def scrape_adidas(url):
    try:
        website = requests.get(url = url, headers={'User-Agent': user_agent_desktop})
    except requests.exceptions.RequestException as e:
        raise SystemExit(e)
    scrape_datetime = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f">> Scraping www.adidas.ch at {scrape_datetime}")
    if website.status_code != 200:
        print(">> Website https://www.adidas.ch is not reachable.")
        print(f">> HTTP request return code: {website}")
    else:
        print(">> Successfully connected to provided URL.")
        soup = BeautifulSoup(website.content, "html.parser")
        scraped_html = soup.find_all("div", attrs={"class": "gl-price gl-price--horizontal notranslate"})
        print(scraped_html)
        # scraped_html_text = scraped_html[0].get_text().strip()
        # if len(scraped_html_text) == 0:
        #     return f"No price was found for given product."
        # else:
        #     scraped_data = {"item": "caran dache rot", "datetime": scrape_datetime, "price": price[0]}
        #     return scraped_data

print(scrape_adidas(url=url[0]))
