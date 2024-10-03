import os

from fastapi import FastAPI
import requests
from dotenv import load_dotenv

load_dotenv()


app = FastAPI()

API_KEY = os.getenv("ALPHA_API")

@app.get("/stock_overview/{stock_name}")
def get_stock_overview(stock_name: str):
    url = f'https://www.alphavantage.co/query?function=OVERVIEW&symbol={stock_name}&apikey={API_KEY}'
    response = requests.get(url)
    data = response.json()
    return data
