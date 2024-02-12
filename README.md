### Description
Code scrapes websites, extracts specific information and then publishes it on a small website

### What code does:
1. Website is created using Flask
2. After server and website is initiated, run src/run_codes.py see if website request returns 200
3. Scrape data and add date time information when it was performed
4. Save data from previous step into a csv file
5. Publish latest data to website

### Running Flask:
as per: https://flask.palletsprojects.com/en/2.0.x/patterns/packages/
`export FLASK_APP=scrape_and_post`
`pip install -e .`
`flask run`