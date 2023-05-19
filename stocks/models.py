from django.db import models

class StockTransaction(models.Model):
    BUY = 'BUY'
    SELL = 'SELL'
    TRANSACTION_TYPES = [
        (BUY, 'Buy'),
        (SELL, 'Sell'),
    ]

    # no company name because calculating for single company
    transaction_date = models.DateField()
    transaction_type = models.CharField(max_length=4, choices=TRANSACTION_TYPES)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.IntegerField()

    def __str__(self):
        return f'{self.transaction_type}'
