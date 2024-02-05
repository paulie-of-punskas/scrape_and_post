# === code runs ./src/scrape_data/run_scrape_codes.py
# === reads saved ./data/scraped_data.csv
# === groups data by items and calculates average price
# === creates below data frame:
# === +-item-+-latest_scrape_datetime-+-newest_price-+-avg_price-+-comment-+
 
import pandas as pd
from flask import jsonify

def output_scraped_data():
    csv_file = pd.read_csv("./scrape_and_post/scraped_data.csv")

    # === group data frame by 'item'
    avg_price = csv_file.groupby(by="item", as_index=False)["price"].mean().rename(columns={"price": "avg_price"})

    # === group by item and price, get latest scrape date and rename columns
    csv_file_grouped = csv_file.groupby(by=["item", "price"], as_index=False)["scrape_datetime"] \
                    .max() \
                    .rename(columns={"price": "newest_price", "scrape_datetime": "latest_scrape_datetime"})

    new_df = pd.merge(left=csv_file_grouped, right=avg_price, on="item")
    new_df = new_df[["item", "latest_scrape_datetime", "newest_price", "avg_price"]]

    new_df["price_lowered"] = new_df.apply(lambda x: "True" if x["newest_price"] < x["avg_price"] else "False", axis=1)
    return jsonify(new_df.to_dict(orient="records"))
