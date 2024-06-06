from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone

from stocks.models import Stock


# Create your models here.

class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.username


class UserStockAlert(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    stock = models.ForeignKey(Stock, on_delete=models.CASCADE)
    alert_price = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.stock.symbol} - {self.alert_price}"

# To resolve the issue and correctly add the created_at field with auto_now_add=True, you should follow a two-step
# migration process. This involves adding the field with a temporary default (default=timezone.now) value first and
# then updating it to use auto_now_add=True
