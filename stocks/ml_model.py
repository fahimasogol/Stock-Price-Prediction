import joblib  # Library to save and load machine learning models.
import os
from django.conf import settings


# load_model Function:

# Constructs the path to the saved model file stock_price_model.pkl.
# Loads the model using joblib and returns it.
def load_model():
    model_path = os.path.join(settings.BASE_DIR, 'scripts', 'stock_price_model.pkl')
    model = joblib.load(model_path)
    return model


# predict_stock_price Function:
#
# Loads the machine learning model.
# Uses the model to predict the stock price for the given day of the year.
# Returns the predicted price.
def predict_stock_price(day_of_year):
    model = load_model()
    prediction = model.predict([[day_of_year]])
    return prediction[0]
