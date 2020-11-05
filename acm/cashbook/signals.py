from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import DayBook, Ledger, CashBook


@receiver(post_save, sender=DayBook)
def post_save_create_cashbook(sender, instance, created, **kwargs):
    if created:
        if instance.credit_or_debit == 'debit':
            b = CashBook.objects.create(
            day_book=instance,
            particulars=f'To {instance.ledger_master} a/c',
            credit_or_debit=instance.credit_or_debit,
            bank_or_cash=instance.bank_or_cash,
            amount=instance.amount
            )
            b.save()
        elif instance.credit_or_debit == 'credit':
            b = CashBook.objects.create(
                day_book=instance,
                credit_or_debit=instance.credit_or_debit,
                particulars=f'By {instance.ledger_master} a/c',
                amount=instance.amount,
                bank_or_cash=instance.bank_or_cash
            )
            b.save()
            return b


@receiver(post_save, sender=DayBook)

def post_save_create_ledger(sender, instance, created, **kwargs):  
    if created:
        z = '' 
        credit_or_debit = ''
        if instance.credit_or_debit == 'credit':
            credit_or_debit = 'debit'
        elif instance.credit_or_debit == 'debit':
            credit_or_debit = 'credit'

        if instance.bank_or_cash == 'bank':
            z = 'To Bank'
        elif instance.bank_or_cash == 'cash':
            z = 'To Cash'

            
        a = Ledger.objects.create(
            ledger_master=instance.ledger_master,
            credit_or_debit=credit_or_debit,
            particulars=z,
            amount=instance.amount,
        )
        a.save()


