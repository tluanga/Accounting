from django.db import models

CHOICES = (
    ("credit", "credit"),
    ("debit", "debit"),
)
class TradingAccount(models.Model):
    credit_or_debit = models.CharField(max_length=50, choices=CHOICES, default=None)
    particulars = models.CharField(max_length=255)
    amount = models.DecimalField(default=0, decimal_places=2, max_digits=12)
    total = models.DecimalField(default=0, decimal_places=2, max_digits=12)

class ProfitAndLossAccount(models.Model):
    credit_or_debit = models.CharField(max_length=50, choices=CHOICES, default=None)
    particulars = models.CharField(max_length=255)
    amount = models.DecimalField(default=0, decimal_places=2, max_digits=12)
    total = models.DecimalField(default=0, decimal_places=2, max_digits=12)
    
class BalanceSheet(models.Model):
    credit_or_debit = models.CharField(max_length=50, choices=CHOICES, default='debit')
    liabilities = models.CharField(max_length=255)
    amount = models.DecimalField(default=0, decimal_places=2, max_digits=12)
    assets = models.CharField(max_length=255)
    total = models.DecimalField(default=0, decimal_places=2, max_digits=12)

