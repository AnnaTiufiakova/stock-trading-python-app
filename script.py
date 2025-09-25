import requests
import os
import csv
from dotenv import load_dotenv
import time

load_dotenv()


POLYGON_API_KEY = os.getenv("POLYGON_API_KEY")

LIMIT = 1000


url = f"https://api.polygon.io/v3/reference/tickers?market=stocks&active=true&order=asc&limit={LIMIT}&sort=ticker&apiKey={POLYGON_API_KEY}"

response = requests.get(url)

tickers = []
data = response.json()

if "results" not in data:
    print("No results found", data)
    exit()

for ticker in data["results"]:
    tickers.append(ticker)

while "next_url" in data:
    print("Getting next page", data["next_url"])
    time.sleep(12)  # sleep for 12 seconds to avoid rate limiting
    response = requests.get(data["next_url"] + f"&apiKey={POLYGON_API_KEY}")
    data = response.json()

    if "results" not in data:
        print("No results found", data)
        break

    for ticker in data["results"]:
        tickers.append(ticker)

example_ticker = {
    "ticker": "HTHT",
    "name": "H World Group Limited American Depositary Shares",
    "market": "stocks",
    "locale": "us",
    "primary_exchange": "XNAS",
    "type": "ADRC",
    "active": True,
    "currency_name": "usd",
    "cik": "0001483994",
    "composite_figi": "BBG000QFPM65",
    "share_class_figi": "BBG001T6Y5T2",
    "last_updated_utc": "2025-09-19T06:05:18.516617619Z",
}

# write to csv with example_ticker schema

fieldnames = list(example_ticker.keys())
output_csv = "tickers.csv"
with open(output_csv, mode="w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    for t in tickers:
        row = {key: t.get(key, "") for key in fieldnames}
        writer.writerow(row)
    print(f"Wrote {len(tickers)} tickers to {output_csv}")
