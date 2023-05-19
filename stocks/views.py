from rest_framework import generics
from .models import StockTransaction
from .serializers import StockTransactionSerializer
from django.db.models import Sum
from rest_framework.response import Response
from django.db import models

class StockSummaryView(generics.ListAPIView):
    serializer_class = StockTransactionSerializer

     

    def list(self, request, *args, **kwargs):
        queryset = StockTransaction.objects.all()
        queryset = queryset.order_by('transaction_date')

        total_qty = total_price = 0

        transaction_list = [[one.quantity, one.price, one.transaction_type] for one in queryset]
        for i in transaction_list:
            if i[2] == 'SELL':
                while i[0] != 0:
                    for j in transaction_list:
                        if j[0] != 0:
                            if j[0] < i[0]:
                                i[0] -= j[0]
                                j[0] = 0
                            else:
                                j[0] -= i[0]
                                i[0] = 0 
                                break
        for i in transaction_list:
            if i[2] != 'SELL':
                total_price += (i[0] * i[1])
                total_qty += i[0]         

        average_buy_price = total_price / total_qty if total_qty > 0 else 0

        response_data = {
            'average_buy_price': round(average_buy_price, 2)
        }

        return Response(response_data)
