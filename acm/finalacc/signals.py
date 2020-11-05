from django.db.models.signals import post_save
from django.dispatch import receiver
from acm.cashbook.models import DayBook
from acm.trial.models import TrialBalance
from .models import TradingAccount, ProfitAndLossAccount, BalanceSheet

@receiver(post_save, sender=DayBook)
def post_save_create_cashbook(sender, instance, created, **kwargs):
    if created:
        b = TradingAccount.objects.create(
        credit_or_debit=instance.credit_or_debit,
        particulars=instance.particulars,
        amount=instance.amount
        )
        b.save()