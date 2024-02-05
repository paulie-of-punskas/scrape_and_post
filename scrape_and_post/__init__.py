from flask import Flask
app = Flask(__name__)

import os
import scrape_and_post.views

basedir = os.getcwd()