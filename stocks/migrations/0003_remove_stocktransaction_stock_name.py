# Generated by Django 4.2.1 on 2023-05-19 09:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stocks', '0002_stocktransaction_delete_stockpurchase'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='stocktransaction',
            name='stock_name',
        ),
    ]
