import json
from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

class CashBookTestCase(APITestCase):
    def test_cashbook(self):
        url = reverse('cashbook')
        data = {"sl_no": "2",
                "credit_or_debit": 'debit',
                "customer_name": "Sam",
                "particulars": "notebook",
                "amount": "50",
                "date":"27/10/2020"
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Account.objects.count(), 1)
        self.assertEqual(Account.objects.get().sl_no, '2')

'''
    class AccountTests(APITestCase):
    def test_create_account(self):
        """
        Ensure we can create a new account object.
        """
        url = reverse('account-list')
        data = {'name': 'DabApps'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Account.objects.count(), 1)
        self.assertEqual(Account.objects.get().name, 'DabApps')
'''