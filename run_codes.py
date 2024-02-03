# === run codes below and save returned content into a list
# === save list as .json

import csv
import os.path
from scrape_air_zermatt import scrapeAirZermatt
from scrape_caran_dache import scrapeCaranDache

strings_to_find = ["Helly Hansen Daybreaker Fleece Jacke - Herren - spruce",
                   "Helly Hansen Daybreaker Fleece Jacke - Herren - schwarz"]

# === append scraped data to scraped_data.csv
if os.path.isfile(os.getcwd() + "/scraped_data.csv") == True:
    with open("scraped_data.csv", 'a', newline='') as csv_file:
        scraped_data = [scrapeAirZermatt(strings_to_find[0]),
                        scrapeAirZermatt(strings_to_find[1]),
                        scrapeCaranDache()]
        writer = csv.writer(csv_file)
        writer.writerows(scraped_data)
else:
    with open("scraped_data.csv", 'w', newline='') as csv_file:
        scraped_data = [["item", "scrape_datetime", "price"],
                        scrapeAirZermatt(strings_to_find[0]),
                        scrapeAirZermatt(strings_to_find[1]),
                        scrapeCaranDache()]
        writer = csv.writer(csv_file)
        writer.writerows(scraped_data)