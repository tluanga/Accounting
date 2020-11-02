from django.db import models

CHOICES = ( 
    ("credit", "credit"), 
    ("debit", "debit"),
)
CHOICES1 = ( 
    ("cash", "cash"), 
    ("bank", "bank"),
)


# class LedgerMaster(models.Model):
#     name = models.CharField(max_length=50, null=True, blank=True)
#     remarks = models.TextField()

#     def __str__(self):
#         return self.name


class DayBook(models.Model):
    sl_no = models.AutoField(primary_key=True)
    ledger_name = models.CharField(max_length=50, unique = True)
    credit_or_debit = models.CharField(max_length=20, choices=CHOICES, default='debit')
    bank_or_cash = models.CharField(max_length=20, choices=CHOICES1, default='cash')
    particulars = models.CharField(max_length=255, default=False)
    amount = models.DecimalField(default=0, decimal_places=2, max_digits=12)
    active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    remarks = models.TextField(blank=True)

    def __str__(self):
        return self.ledger_name


class Ledger(models.Model):
    name = models.CharField(max_length=50)
    credit_or_debit = models.CharField(max_length=20, choices=CHOICES, default='debit')
    particulars = models.CharField(max_length=255)
    amount = models.DecimalField(default=0, max_digits=12, decimal_places=2)
    active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class CashBook(models.Model):
    sl_no = models.AutoField(primary_key=True)
    particulars = models.CharField(max_length=255, default=False)
    credit_or_debit = models.CharField(max_length=20, choices=CHOICES, default='debit')
    bank_or_cash = models.CharField(max_length=20, choices=CHOICES1, default='cash')
    amount = models.DecimalField(default=0, decimal_places=2, max_digits=12)
    active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)










