from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import DayBook, Ledger, CashBook

@receiver(post_save, sender=DayBook)
def post_save_create_ledger(sender, instance, created, **kwargs):
    if created:
        a = Ledger.objects.create(
            credit_or_debit=not(instance.credit_or_debit),
            ledger_name=instance.ledger,
            amount=instance.amount,
         )
        a.save()
        print(instance.ledger)

@receiver(post_save, sender=DayBook)
def post_save_create_cashbook(sender, instance, created, **kwargs):
    if created:
        b = CashBook.objects.create(
            particulars=instance.particulars,
            amount=instance.amount
        )
        b.save()
