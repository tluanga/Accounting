from django.db import models

CHOICES = ( 
    ("credit", "credit"), 
    ("debit", "debit"),
)
# CHOICES1 = ( 
#     ("cash", "cash"), 
#     ("bank", "bank"),
# )

class TrialBalance(models.Model):
    particulars = models.CharField(max_length=50)
    credit_or_debit = models.CharField(max_length=20, choices=CHOICES, default='debit')
    amount = models.DecimalField(default=0, max_digits=12, decimal_places=2)
    active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
