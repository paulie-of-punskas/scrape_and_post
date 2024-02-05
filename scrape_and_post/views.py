from scrape_and_post import app
from scrape_and_post import src


# a simple page that says hello
@app.route('/hello')
def hello():
    return 'Hello, World!'
    
@app.route('/')
def hello_world():
    return "Laba diena."

@app.route('/scrape')
def scrape_results():
    return src.analyze_data.output_scraped_data()