import datetime
import requests
import os
from dotenv import load_dotenv
import time
import snowflake.connector

load_dotenv()

POLYGON_API_KEY = os.getenv("POLYGON_API_KEY")
LIMIT = 1000
DS = datetime.datetime.now().strftime("%Y-%m-%d")

url = f"https://api.polygon.io/v3/reference/tickers?market=stocks&active=true&order=asc&limit={LIMIT}&sort=ticker&apiKey={POLYGON_API_KEY}"

response = requests.get(url)
tickers = []
data = response.json()

if "results" not in data:
    print("No results found", data)
    exit()

# Add ds column to each row
for ticker in data["results"]:
    ticker["ds"] = DS
tickers.extend(data["results"])

while "next_url" in data:
    print("Getting next page", data["next_url"])
    time.sleep(12)  # avoid rate limiting
    response = requests.get(data["next_url"] + f"&apiKey={POLYGON_API_KEY}")
    data = response.json()

    if "results" not in data:
        print("No results found", data)
        break

    for ticker in data["results"]:
        ticker["ds"] = DS
    tickers.extend(data["results"])

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
    "ds": DS,  # <-- dynamic instead of hardcoded
}


def load_to_snowflake(rows, fieldnames, batch_size=500):
    connect_kwargs = {
        "user": os.getenv("SNOWFLAKE_USER"),
        "password": os.getenv("SNOWFLAKE_PASSWORD"),
    }

    account = os.getenv("SNOWFLAKE_ACCOUNT")
    if account:
        connect_kwargs["account"] = account

    warehouse = os.getenv("SNOWFLAKE_WAREHOUSE")
    database = os.getenv("SNOWFLAKE_DATABASE")
    schema = os.getenv("SNOWFLAKE_SCHEMA")
    role = os.getenv("SNOWFLAKE_ROLE")

    if warehouse:
        connect_kwargs["warehouse"] = warehouse
    if database:
        connect_kwargs["database"] = database
    if schema:
        connect_kwargs["schema"] = schema
    if role:
        connect_kwargs["role"] = role

    conn = snowflake.connector.connect(**connect_kwargs)
    cs = conn.cursor()

    insert_stmt = f"""
    INSERT INTO stock_tickers ({", ".join(fieldnames)})
    VALUES ({", ".join(["%s"] * len(fieldnames))})
    """

    values = [[row.get(col, None) for col in fieldnames] for row in rows]
    for i in range(0, len(values), batch_size):
        batch = values[i : i + batch_size]
        cs.executemany(insert_stmt, batch)

    conn.commit()
    cs.close()
    conn.close()


fieldnames = list(example_ticker.keys())

print(f"Fetched {len(tickers)} rows from Polygon API")
load_to_snowflake(tickers, fieldnames)
print(f"Loaded {len(tickers)} rows into Snowflake table stock_tickers with ds={DS}")
