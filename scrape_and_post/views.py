from scrape_and_post import app
from scrape_and_post.src.analyze_data.output_scraped_data import output_scraped_data
from scrape_and_post.src.scrape_data.run_scrape_codes import run_scrape_codes
from flask import make_response, render_template_string
import pandas
from datetime import datetime

import os


@app.route('/')
def hello_world():
    scrape_datetime = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(scrape_datetime)
    return f"Laba diena, siandien yra {scrape_datetime}"

# run scraping codes
@app.route('/scrape_new_data')
def scrape_results():
    run_scrape_codes()
    return "New data was scraped."
    
@app.route('/view_scraped_data')
def show_scrape_results():
    df_html = output_scraped_data().to_html()
    # resp = make_response(render_template_string(df_html))
    return df_html

@app.route('/csv_exists')
def csv_exists():
    return str(os.path.isfile("./scrape_and_post/data/scraped_data.csv"))

@app.route('/dirs')
def dirs():
    return os.listdir()