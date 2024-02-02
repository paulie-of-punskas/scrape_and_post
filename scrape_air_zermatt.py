# === scrape websites and extract specific information
import requests
from bs4 import BeautifulSoup
from datetime import datetime

# ==== check if URLs respond 200
url = "https://www.air-zermatt.ch/de/air-zermatt/onlineshop/bekleidung/"
strings_to_find = ["Helly Hansen Daybreaker Fleece Jacke - Herren - spruce",
                   "Helly Hansen Daybreaker Fleece Jacke - Herren - schwarz"]

def scrape_air_zermatt(search_string):
    website = requests.get(url = url)
    scrape_datetime = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f">> Scraping air-zermatt.ch at {scrape_datetime}")
    if website.status_code != 200:
        print(">> Website https://www.air-zermatt.ch/ is not reachable.")
        print(f">> HTTP request return code: {website}")
    else:
        print(">> Successfully connected to provided URL.")
        soup = BeautifulSoup(website.content, "html.parser")
        # print(soup.find_all("div", attrs={"class": "shop-price-list shop-price-overview"}))
        # print(soup.find_all("div", attrs={"id": "article_price_304"}))
        scraped_html_code = soup.find_all("div", attrs={"title": search_string})
        if len(scraped_html_code) == 0:
            return f"No price was found for {search_string}."
        else:
            price = scraped_html_code[0].find_all("span", attrs={"class": "price_value"})
            scraped_data = {"item": search_string, "datetime": scrape_datetime, "price": price[0].get_text()}
            return scraped_data

        # for line in url_content:
        #     if re.search(strings_to_find[0], line):
        #         print(line)
        # find location for string containing strings_to_find element and start
        # looping from its location until <span class="price_value"> tag is found

print(scrape_air_zermatt(strings_to_find[0]))
print(scrape_air_zermatt(strings_to_find[1]))
print(scrape_air_zermatt("ai3tuh4i"))
# print(len(scrape_air_zermatt("bastrys")))