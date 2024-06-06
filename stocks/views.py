from rest_framework import viewsets
from .models import Stock, StockPrice
from .serializers import StockSerializer, StockPriceSerializer
from rest_framework import viewsets, status
from rest_framework.response import Response
from datetime import datetime
from .ml_model import predict_stock_price


class StockViewSet(viewsets.ModelViewSet):
    queryset = Stock.objects.all()
    serializer_class = StockSerializer


class StockPriceViewSet(viewsets.ModelViewSet):
    queryset = StockPrice.objects.all()
    serializer_class = StockPriceSerializer


class StockPredictionViewSet(viewsets.ViewSet):
    def retrieve(self, request, pk=None):
        try:
            stock = Stock.objects.get(pk=pk)
            today = datetime.today()
            day_of_year = today.timetuple().tm_yday  # .tm_yday: The tm_yday attribute of the time.struct_time object
            # represents the day of the year as an integer (ranging from 1 to 365, or 1 to 366 for leap years)
            predicted_price = predict_stock_price(day_of_year)
            return Response({'symbol': stock.symbol, 'predicted_price': predicted_price}, status=status.HTTP_200_OK)
        except Stock.DoesNotExist:
            return Response({'error': 'Stock not found'}, status=status.HTTP_404_NOT_FOUND)
