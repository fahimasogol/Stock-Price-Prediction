from rest_framework.response import Response
from rest_framework import viewsets, status
from rest_framework.views import APIView

from stocks.models import Stock
from .models import CustomUser, UserStockAlert
from .serializers import CustomUserSerializer, UserStockAlertSerializer


class CustomUserViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer


class SetAlertAPIView(APIView):
    def post(self, request, *args, **kwargs):
        user = request.user
        stock_id = request.data.get('stock_id')
        alert_price = request.data.get('alert_price')

        try:
            stock = Stock.objects.get(id=stock_id)
        except Stock.DoesNotExist:
            return Response({'error': 'Stock not found'}, status=status.HTTP_404_NOT_FOUND)

        alert = UserStockAlert.objects.create(user=user, stock=stock, alert_price=alert_price)
        serializer = UserStockAlertSerializer(alert)
        return Response({'status': 'alert set', 'alert_id': alert.id, 'alert': serializer.data},
                        status=status.HTTP_201_CREATED)


# from rest_framework.decorators import api_view
#
#
# @api_view(['GET', 'POST'])
# def test_view(request):
#     print(f"Request method: {request.method}")  # Log the request method
#     if request.method == 'POST':
#         print("POST data:", request.data)  # Log the POST data
#         return Response({'message': 'POST method is working'}, status=status.HTTP_200_OK)
#     print("GET request received")
#     return Response({'message': 'GET method is working'}, status=status.HTTP_200_OK)
