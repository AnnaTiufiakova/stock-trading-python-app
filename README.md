# Stock Trading Data Extractor

A Python pipeline that connects to the Polygon.io (https://polygon.io/) REST API to extract live stock ticker data, handle pagination, and store the results in Snowflake for downstream analysis.

## 🚀 Features<br>
 • Python for data extraction and automation<br>
 • REST API integration with Polygon.io<br>
 • Pagination handling with next_url to fetch multiple API pages<br>
 • Rate limiting controls using time.sleep() to respect API limits<br>
 • Data ingestion into Snowflake using batch inserts for performance<br>
 • Scheduling with the schedule library (future step: Airflow or GitHub Actions)

## 📂 Project Structure
 
├── script.py          # Extracts stock tickers and saves to CSV<br>
├── tickers.csv        # Output data (generated after running script)<br>
├── .env               # Stores API key and Snowflake credentials (not committed to repo)<br>
├── requirements.txt   # Python dependencies<br>
└── README.md          # Project documentation

## ⚙️ Setup & Installation

1. Clone the repo:
```
git clone https://github.com/AnnaTiufiakova/stock-trading-python-app.git
cd stock-trading-python-app
```

2. Create a virtual environment & install dependencies:
```
python -m venv pythonenv
source pythonenv/bin/activate   # Mac/Linux
pythonenv\Scripts\activate      # Windows
pip install -r requirements.txt
```

3. Add your Polygon.io API key and Snowflake credentialsto a .env file:
```
POLYGON_API_KEY=your_api_key_here
SNOWFLAKE_USER=your_user
SNOWFLAKE_PASSWORD=your_password
SNOWFLAKE_ACCOUNT=your_account
SNOWFLAKE_DATABASE=your_database
SNOWFLAKE_SCHEMA=your_schema
SNOWFLAKE_WAREHOUSE=your_warehouse
SNOWFLAKE_ROLE=your_role
```
## ▶️ Usage:

Run extraction manually:
```
python script.py
```
This will fetch stock tickers from Polygon.io and insert them into the stock_tickers table in Snowflake

## ⚙️ Tech Stack<br>
 • Python → Data extraction & automation<br>
 • Requests → API communication<br>
 • dotenv → Manage API keys securely<br>
 • Snowflake → Cloud data warehouse for scalable storage and querying <br>
 • time.sleep() → Rate limiting control

## 🔜 Planned:<br>
 • Apache Airflow / GitHub Actions → Automated scheduling<br>
 • Amazon S3 → Alternative scalable storage solution


