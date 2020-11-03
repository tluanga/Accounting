from django.db import models
from django.db.models import Sum
import time, datetime


CHOICES = ( 
    ("credit", "credit"), 
    ("debit", "debit"),
)
CHOICES1 = ( 
    ("cash", "cash"), 
    ("bank", "bank"),
)


class LedgerMaster(models.Model):
     name = models.CharField(max_length=50, null=True, blank=True)
     remarks = models.TextField()

     def __str__(self):
         return self.name


class DayBook(models.Model):
    ledger_master = models.ForeignKey(LedgerMaster, on_delete=models.DO_NOTHING)
    credit_or_debit = models.CharField(max_length=20, choices=CHOICES, default='debit')
    bank_or_cash = models.CharField(max_length=20, choices=CHOICES1, default='cash')
    particulars = models.CharField(max_length=255, default=False)
    amount = models.DecimalField(default=0, decimal_places=2, max_digits=12)
    active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    remarks = models.TextField(blank=True)


class Ledger(models.Model):
    ledger_master = models.ForeignKey(LedgerMaster, on_delete=models.CASCADE)
    credit_or_debit = models.CharField(max_length=20, choices=CHOICES, default='debit')
    particulars = models.CharField(max_length=255)
    amount = models.DecimalField(default=0, max_digits=12, decimal_places=2)
    active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    @staticmethod
    def update_trial_balance(ledger_master, start_date, end_date):
        data = Ledger.objects.filter(
            ledger_master=ledger_master,
            created_at=start_date,
            updated_at=end_date
        ).aggregate(Sum('amount'))
        return data



class CashBook(models.Model):
    day_book = models.ForeignKey(DayBook, on_delete=models.CASCADE)
    particulars = models.CharField(max_length=255, default=False)
    credit_or_debit = models.CharField(max_length=20, choices=CHOICES, default='debit')
    bank_or_cash = models.CharField(max_length=20, choices=CHOICES1, default='cash')
    amount = models.DecimalField(default=0, decimal_places=2, max_digits=12)
    active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

