# Generated by Django 3.1.3 on 2020-11-04 08:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TrialBalance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('particulars', models.CharField(max_length=50)),
                ('credit_or_debit', models.CharField(choices=[('credit', 'credit'), ('debit', 'debit')], default='debit', max_length=20)),
                ('amount', models.DecimalField(decimal_places=2, default=0, max_digits=12)),
                ('active', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
