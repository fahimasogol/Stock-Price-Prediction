"""
URL configuration for main project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from stocks.views import StockViewSet, StockPriceViewSet, StockPredictionViewSet
from users.views import CustomUserViewSet

router = routers.DefaultRouter()
router.register(r'stocks', StockViewSet)
router.register(r'stock-prices', StockPriceViewSet)
router.register(r'stock-predictions', StockPredictionViewSet, basename='stock-prediction')
router.register(r'users', CustomUserViewSet)
# router.register(r'user-stock-alerts', UserStockAlertViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls')),
    path('api/users/', include('users.urls'))
]
