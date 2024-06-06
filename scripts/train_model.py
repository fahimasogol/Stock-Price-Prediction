import os
import sys
import django
import pandas as pd
from sklearn.linear_model import LinearRegression
import joblib
from datetime import datetime

# Add the project base directory to the Python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Setup Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'main.settings')
django.setup()
# Sets the DJANGO_SETTINGS_MODULE environment variable to point to your Django settings.
# Calls django.setup() to initialize Django

from stocks.models import StockPrice
from django.conf import settings


# The goal is to predict the closing price of the stock based on the day of the year
def train_model():
    # Fetch data from the database
    data = list(StockPrice.objects.values('date', 'close_price'))  # Fetches stock price data from the StockPrice model.
    df = pd.DataFrame(data)  # Converts the data into a pandas DataFrame.
    df['date'] = pd.to_datetime(df['date'])
    df = df.sort_values('date')

    # Create features and target
    df['day'] = df['date'].dt.dayofyear # This expression converts each date to the corresponding day of the year (an
    # integer between 1 and 365 or 366 for leap years
    X = df[['day']] # X: This is the feature matrix (independent variable). It consists of the day column we just
    # created.
    y = df['close_price'] # y: This is the target vector (dependent variable). It consists of the close_price column
    # from the DataFrame.

    # Train the model
    model = LinearRegression()
    model.fit(X, y)

    # Save the model
    model_path = os.path.join(settings.BASE_DIR, 'scripts', 'stock_price_model.pkl')
    joblib.dump(model, model_path)


if __name__ == '__main__':
    train_model()
