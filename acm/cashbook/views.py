from django.shortcuts import render

from rest_framework import viewsets
from .models import DayBook, Ledger, CashBook
from .serializers import DayBookSerializer, LedgerSerializer, CashBookSerializer

# class LedgerMasterViewSet(viewsets.ModelViewSet):
#     queryset = LedgerMaster.objects.all()
#     serializer_class = LedgerMasterSerializer

class DayBookViewSet(viewsets.ModelViewSet):
    queryset = DayBook.objects.all()
    serializer_class = DayBookSerializer

class LedgerViewSet(viewsets.ModelViewSet):
    queryset = Ledger.objects.all()
    serializer_class = LedgerSerializer

class CashBookViewSet(viewsets.ModelViewSet):
    queryset = CashBook.objects.all()
    serializer_class = CashBookSerializer



    

