from django.urls import path
from .views import StockSummaryView, AddStock

app_name = 'stocks'

urlpatterns = [
    path('stock-summary/', StockSummaryView.as_view(), name='stock_summary'),
    path('add-stock/', AddStock.as_view(), name='add-stock'),

]
