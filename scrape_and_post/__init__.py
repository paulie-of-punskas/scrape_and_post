from flask import Flask
app = Flask(__name__)

import scrape_and_post.views
