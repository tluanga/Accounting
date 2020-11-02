from django.db.models.signals import post_save
from django.dispatch import receiver
from acm.cashbook.models import DayBook
from .models import TrialBalance


@receiver(post_save, sender=DayBook)
def post_save_create_trial_balance(sender, instance, created, **kwargs):
    if created:
        z = f'{instance.particulars} a/c'
        c = TrialBalance.objects.create(
            particulars=z,
            credit_or_debit=instance.credit_or_debit,
            amount=instance.amount,
        )
        c.save()
