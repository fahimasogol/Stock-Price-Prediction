import requests
from django.core.management.base import BaseCommand  # Django class for creating custom management commands.
from stocks.models import Stock, StockPrice
from datetime import datetime

API_KEY = 'TPKMCM32HZZ8YIYR'
BASE_URL = 'https://www.alphavantage.co/query'


class Command(BaseCommand):
    help = 'Fetch and store stock data'

    def handle(self, *args, **kwargs):  # The main method that executes when the command is run.
        print("Fetching stock data...")  # Debugging statement
        stocks = Stock.objects.all()  # Retrieves all stocks from the database
        if not stocks.exists():
            print("No stocks found in the database.")  # Debugging statement
            return

        for stock in stocks:
            print(f"Fetching data for {stock.symbol}...")  # Debugging statement
            response = requests.get(BASE_URL, params={
                'function': 'TIME_SERIES_DAILY',
                'symbol': stock.symbol,
                'apikey': API_KEY
            }, proxies={})  # Disable proxy

            if response.status_code != 200:
                print(f"Error fetching data: {response.status_code} - {response.text}")  # Debugging statement
                self.stdout.write(self.style.ERROR(f"Error fetching data for {stock.symbol}"))
                continue

            print(f"Response received for {stock.symbol}: {response.json()}")  # Debugging statement
            data = response.json().get('Time Series (Daily)', {})
            if not data:
                print(f"No data found for {stock.symbol}.")  # Debugging statement
                continue

            for date, prices in data.items():
                StockPrice.objects.update_or_create(
                    stock=stock,
                    date=datetime.strptime(date, '%Y-%m-%d'),
                    defaults={
                        'open_price': prices['1. open'],
                        'high_price': prices['2. high'],
                        'low_price': prices['3. low'],
                        'close_price': prices['4. close'],
                        'volume': prices['5. volume']
                    }
                )
            self.stdout.write(self.style.SUCCESS(f"Successfully fetched data for {stock.symbol}"))
