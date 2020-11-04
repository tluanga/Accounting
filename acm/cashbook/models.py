from django.db import models
from django.db.models import Sum
import time, datetime
from acm.trial.models import TrialBalance


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

    # @staticmethod
    # def update_trial_balance(ledger_master, start_date, end_date):
    #     data = Ledger.objects.filter(
    #         ledger_master=ledger_master,
    #         created_at__gte=start_date,
    #         created_at__lte=end_date
    #     ).aggregate(Sum('amount'))
    #     return data
    
    @staticmethod
    def update_trial_balance(ledger_master, start_date, end_date):
        new_amount = Ledger.objects.filter(
            ledger_master=ledger_master,
            created_at__gte=start_date,
            created_at__lte=end_date
        ).aggregate(Sum('amount'))

        ledger_master_object = TrialBalance.objects.filter(id=ledger_master)
        
        if ledger_master_object.exists():
            updated_data = TrialBalance.objects.update(
                particulars=ledger_master,
                amount=new_amount                
            )
            updated_data.save()
            return updated_data

        elif ledger_master_object.DoesNotExist:
            updated_data = TrialBalance.objects.create(
                particulars=ledger_master,
                credit_or_debit=credit_or_debit,
                amount=new_amount
            )
            updated_data.save()
            return updated_data


class CashBook(models.Model):
    day_book = models.ForeignKey(DayBook, on_delete=models.CASCADE)
    particulars = models.CharField(max_length=255, default=False)
    credit_or_debit = models.CharField(max_length=20, choices=CHOICES, default='debit')
    bank_or_cash = models.CharField(max_length=20, choices=CHOICES1, default='cash')
    amount = models.DecimalField(default=0, decimal_places=2, max_digits=12)
    active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

