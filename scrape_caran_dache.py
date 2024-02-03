# === scrape websites and extract specific information
import requests
import re
from bs4 import BeautifulSoup
from datetime import datetime

url = "https://www.carandache.com/ch/de/patronen/patrone-goliath-kugelschreiber-849-rot-m-f-p-10224.htm"

# Windows 10 with Google Chrome
user_agent_desktop = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '\
'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 '\
'Safari/537.36'

def scrapeCaranDache():
    try:
        website = requests.get(url = url, headers={'User-Agent': user_agent_desktop})
    except requests.exceptions.RequestException as e:
        raise SystemExit(e)
    scrape_datetime = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f">> Scraping www.carandache.com at {scrape_datetime}")
    if website.status_code != 200:
        print(">> Website https://www.carandache.com is not reachable.")
        print(f">> HTTP request return code: {website}")
    else:
        print(">> Successfully connected to provided URL.")
        soup = BeautifulSoup(website.content, "html.parser")
        scraped_html = soup.find_all("h2", attrs={"class": "best"})
        scraped_html_text = scraped_html[0].get_text().strip()
        if len(scraped_html_text) == 0:
            return f"No price was found for given product."
        else:
            print(">> Successfully scraped carandache.com")
            price = re.findall('[\d]*[.][\d]+', scraped_html_text)
            # use regex to extract 7.80 string
            # scraped_data = {"item": "caran dache rot", "scrape_datetime": scrape_datetime, "price": price[0]}
            scraped_data = ("caran dache rot", scrape_datetime, price[0])
            return scraped_data
