from django.db.models.signals import post_save
from django.dispatch import receiver
from acm.cashbook.models import DayBook
from .models import TrialBalance


@receiver(post_save, sender=DayBook)
def post_save_create_trial_balance(sender, instance, created, **kwargs):
    if created:
        credit_or_debit = ''
        if instance.credit_or_debit == 'credit':
            credit_or_debit = 'debit'
        elif instance.credit_or_debit == 'debit':
            credit_or_debit = 'credit'

        c = TrialBalance.objects.create(
            particulars=f'{instance.ledger_name} a/c',
            credit_or_debit=credit_or_debit,
            amount=instance.amount,
        )
        c.save()