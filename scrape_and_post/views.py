from scrape_and_post import app
from scrape_and_post.src.analyze_data.output_scraped_data import output_scraped_data
from scrape_and_post.src.scrape_data.run_scrape_codes import run_scrape_codes
from flask import make_response, render_template, url_for
import pandas
from datetime import datetime
import os


@app.route('/')
def index():
    current_datetime = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    df = output_scraped_data()

    # === check if all price_lowered values are "True"/"False"
    if (df["price_lowered"].any() == True):
        any_price_lowered = True
    else:
        any_price_lowered = False

    return render_template("index.html", current_datetime=current_datetime, any_price_lowered=any_price_lowered)
    # return render_template("index.html", scrape_datetime=scrape_datetime, df_html=df_html)

# run scraping codes
@app.route('/scrape_new_data')
def scrape_results():
    run_scrape_codes()
    return "New data was scraped."
    
@app.route('/view_scraped_data_old')
def show_scrape_results():
    df_html = output_scraped_data().to_html()
    # resp = make_response(render_template_string(df_html))
    return df_html

@app.route('/view_scraped_data')
def show_scrape_results2():
    df = output_scraped_data()
    # === convert pandas dataframe to list -- this will later be used for printing df values to html
    df_as_list = list(df.values.tolist())
    return render_template("view_scraped_data.html", df=df, df_as_list=df_as_list, zip=zip)

@app.route('/csv_exists')
def csv_exists():
    return str(os.path.isfile("./scrape_and_post/data/scraped_data.csv"))

@app.route('/dirs')
def dirs():
    return os.listdir()