# === nemeta moduleerror kaip paleidziama yra su:
# python3 -m unittest tests.test_scrape_air_zermatt
# arba su:
# python -m pytest
from src.scrape_data.scrape_air_zermatt import scrapeAirZermatt
import unittest

class TestAirZermatt(unittest.TestCase):

    def test_old_string(self):
        strings_to_find = ["Helly Hansen Daybreaker Fleece Jacke - Herren - spruce", 
                   "Helly Hansen Daybreaker Fleece Jacke - Herren - schwarz"]
        self.assertEqual(scrapeAirZermatt(strings_to_find[0]), "No price was found for Helly Hansen Daybreaker Fleece Jacke - Herren - spruce.")
        self.assertEqual(scrapeAirZermatt(strings_to_find[1]), "No price was found for Helly Hansen Daybreaker Fleece Jacke - Herren - schwarz.")

    def test_new_string(self):
        strings_to_find = "Helly Hansen Fleece Jacke - Herren - spruce"
        self.assertTrue(scrapeAirZermatt(strings_to_find) != "No price was found for Helly Hansen Daybreaker Fleece Jacke - Herren - spruce.")

# print(scrapeAirZermatt(strings_to_find[0]))
# print(scrapeAirZermatt(strings_to_find[1]))
# print(scrapeAirZermatt(strings_to_find[2]))

def test_sample():
    return("ksahdfiseudhiu")

# import requests
# from bs4 import BeautifulSoup
# from datetime import datetime
# url = "https://www.air-zermatt.ch/de/air-zermatt/onlineshop/bekleidung/"
# user_agent_desktop = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '\
# 'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 '\
# 'Safari/537.36'
# website = requests.get(url = url, headers={'User-Agent': user_agent_desktop})
# soup = BeautifulSoup(website.content, "html.parser")
# scraped_html_code = soup.find_all("div", attrs={"title": strings_to_find[0]})
# print(soup)