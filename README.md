# Stock Trading Data Extractor

A Python pipeline that connects to the Polygon.io (https://polygon.io/) REST API to extract live stock ticker data, handle pagination, and store the results in CSV format for downstream analysis.

## 🚀 Features<br>
 • Python for data extraction and automation<br>
 • REST API integration with Polygon.io<br>
 • Pagination handling with next_url to fetch multiple API pages<br>
 • Rate limiting controls using time.sleep() to respect API limits<br>
 • JSON → CSV conversion using a defined example_ticker schema for clean structured outputs<br>
 • Scheduling with the schedule library (future step: Airflow or GitHub Actions)

## 📂 Project Structure
 
├── script.py          # Extracts stock tickers and saves to CSV<br>
├── tickers.csv        # Output data (generated after running script)<br>
├── .env               # Stores Polygon.io API key (not committed to repo)<br>
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
python -m venv venv
source venv/bin/activate   # Mac/Linux
venv\Scripts\activate      # Windows
pip install -r requirements.txt
```

3. Add your Polygon.io API key to a .env file:
```
POLYGON_API_KEY=your_api_key_here
```
## ▶️ Usage:

Run extraction manually:
```
python script.py
```

## ⚙️ Tech Stack<br>
 • Python → Data extraction & automation<br>
 • Requests → API communication<br>
 • dotenv → Manage API keys securely<br>
 • CSV → Current storage format<br>
 • time.sleep() → Rate limiting control

## 🔜 Planned:<br>
 • Apache Airflow / GitHub Actions → Automated scheduling<br>
 • PostgreSQL / Amazon S3 → Scalable storage solution


