from django.urls import path
from .views import StockSummaryView

app_name = 'stocks'

urlpatterns = [
    path('stock-summary/', StockSummaryView.as_view(), name='stock_summary'),
]
