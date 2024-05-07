FROM python:3.9.6

COPY ./requirements.txt /app/requirements.txt

WORKDIR /app

RUN python -m pip install -r requirements.txt

COPY . /app

# add RW permissions to .csv file
RUN chmod 755 /app

# Expose the port that the application listens on.
EXPOSE 5001

# Register application
ENV FLASK_APP=scrape_and_post

# Run Flask app
CMD python3 -m flask run --host=0.0.0.0
