# === run codes below and save returned content into a list
# === save list as .json
import csv
import os.path
from scrape_and_post.src.scrape_data.scrape_air_zermatt import scrapeAirZermatt
from scrape_and_post.src.scrape_data.scrape_caran_dache import scrapeCaranDache

def run_scrape_codes():
    strings_to_find = ["Helly Hansen Daybreaker Fleece Jacke - Herren - spruce",
                       "Helly Hansen Daybreaker Fleece Jacke - Herren - schwarz",
                       "Helly Hansen Fleece Jacke - Herren - spruce",
                       "Helly Hansen Fleece Jacke - Herren - schwarz"]

    scraped_data = [scrapeAirZermatt(strings_to_find[0]),
                    scrapeAirZermatt(strings_to_find[1]),
                    scrapeAirZermatt(strings_to_find[2]),
                    scrapeAirZermatt(strings_to_find[3]),
                    scrapeCaranDache()]

    # === append scraped data, append new information and save it as scraped_data.csv
    if os.path.isfile("./scrape_and_post/data/scraped_data.csv") == True:
        with open("./scrape_and_post/data/scraped_data.csv", 'a', newline='') as csv_file:
            writer = csv.writer(csv_file)
            writer.writerows(scraped_data)
    else:
        with open("./scrape_and_post/data/scraped_data.csv", 'w', newline='') as csv_file:
            writer = csv.writer(csv_file)
            writer.writerows(scraped_data)
    return "New data was scraped."
