from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import DayBook, Ledger, CashBook


@receiver(post_save, sender=DayBook)

def post_save_create_ledger(sender, instance, created, **kwargs):  
    if created:
        credit_or_debit = ''
        if instance.credit_or_debit == 'credit':
            credit_or_debit = 'debit'
        elif instance.credit_or_debit == 'debit':
            credit_or_debit = 'credit'
            
        a = Ledger.objects.create(
            credit_or_debit=credit_or_debit,
            ledger_name=instance.ledger,
            particulars=instance.particulars,
            amount=instance.amount,
        )
        a.save()
        print(instance.ledger)

@receiver(post_save, sender=DayBook)
def post_save_create_cashbook(sender, instance, created, **kwargs):
    if created:
        b = CashBook.objects.create(
            particulars=instance.particulars,
            amount=instance.amount,
        )
        b.save()
