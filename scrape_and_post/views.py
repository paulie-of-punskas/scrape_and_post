from scrape_and_post import app
from scrape_and_post.output_scraped_data import output_scraped_data

import os

# a simple page that says hello
@app.route('/hello')
def hello():
    return 'Hello, World!'
    
@app.route('/')
def hello_world():
    return "Laba diena."

@app.route('/scrape')
def scrape_results():
    xx = "tetstestgerjgserj"
    return output_scraped_data()

@app.route('/dirs')
def dirs():
    return os.listdir()