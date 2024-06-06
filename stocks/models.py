from django.db import models


class Stock(models.Model):
    symbol = models.CharField(max_length=10)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.symbol


class StockPrice(models.Model):
    stock = models.ForeignKey(Stock, on_delete=models.CASCADE)
    date = models.DateField()
    open_price = models.FloatField()
    high_price = models.FloatField()
    low_price = models.FloatField()
    close_price = models.FloatField()
    volume = models.BigIntegerField()
