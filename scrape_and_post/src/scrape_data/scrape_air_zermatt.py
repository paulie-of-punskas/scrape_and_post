# === scrape websites and extract specific information
import requests
from bs4 import BeautifulSoup
from datetime import datetime

# ==== check if URLs respond 200
url = "https://www.air-zermatt.ch/de/air-zermatt/onlineshop/bekleidung/"

user_agent_desktop = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '\
'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 '\
'Safari/537.36'

def scrapeAirZermatt(search_string):
    try:
        website = requests.get(url = url, headers={'User-Agent': user_agent_desktop})
    except requests.exceptions.RequestException as e:
        raise SystemExit(e)
    scrape_datetime = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f">> Scraping air-zermatt.ch at {scrape_datetime}")
    if website.status_code != 200:
        print(">> Website https://www.air-zermatt.ch is not reachable.")
        print(f">> HTTP request return code: {website}")
    else:
        print(">> Successfully connected to provided URL.")
        soup = BeautifulSoup(website.content, "html.parser")
        # print(soup.find_all("div", attrs={"class": "shop-price-list shop-price-overview"}))
        # print(soup.find_all("div", attrs={"id": "article_price_304"}))
        scraped_html_code = soup.find_all("div", attrs={"title": search_string})
        if len(scraped_html_code) == 0:
            scraped_data = (search_string, scrape_datetime, "No price found or scraping error")
            print(f"No price was found for {search_string}.")
        else:
            print(">> Successfully scraped air-zermatt.ch")
            price = scraped_html_code[0].find_all("span", attrs={"class": "price_value"})
            # scraped_data = {"item": search_string, "scrape_datetime": scrape_datetime, "price": price[0].get_text()}
            scraped_data = (search_string, scrape_datetime, price[0].get_text())
        return scraped_data
