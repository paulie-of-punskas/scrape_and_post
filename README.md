### Description
Code scrapes websites, extracts specific information and then publishes it on a small website

### What code does:
1. Website is created using Flask
2. After server and website is initiated, run src/run_codes.py see if website request returns 200
3. Scrape data and add date time information when it was performed
4. Save data from previous step into a csv file
5. Publish latest data to website

### Running locally:
as per: https://flask.palletsprojects.com/en/2.0.x/patterns/packages/
`export FLASK_APP=scrape_and_post`
`pip install -e .`
`flask run`

### Running in Docker container:
As per README.Docker.md: 
- build image: `docker compose up --build`
- run app on 5001 port: `docker run -p 5001:5000 -d scrape_and_post`

#### Alternative way, to run it on port 5001:
- `flask run -h localhost -p 5001`
- `docker build --tag scrape_and_post .`
    - `docker run -p 5000:5000 -d scrape_and_post` or 
    - `docker run -p 5001:5000 -d scrape_and_post`

### Running tests:
- navigate to `./scrape_and_post/scrape_and_post`
- example unit test call: `python3 -m unittest tests.test_scrape_air_zermatt`

## View app logs:
- get running containers: `docker ps`
- get logs of running container: `docker logs ####`

### Known problems:
- endpoint `/scrape_new_data` returns error

### To do:
- update string following strings, to regex pattern:
    - Helly Hansen Daybreaker Fleece Jacke - Herren - spruce
    - Helly Hansen Fleece Jacke - Herren - spruce
- add [SIX APIs](https://web.apiportal.six-group.com/portal/bfi/catalog)