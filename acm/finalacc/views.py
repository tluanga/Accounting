from django.shortcuts import render
from rest_framework import viewsets
from .models import TradingAccount, ProfitAndLossAccount, BalanceSheet
from .serializers import TradingAccountSerializer, ProfitAndLossAccountSerializer, BalanceSheetSerializer

class TradingAccountViewSet(viewsets.ModelViewSet):
    queryset = TradingAccount.objects.all()
    serializer_class = TradingAccountSerializer

class ProfitAndLossAccountViewSet(viewsets.ModelViewSet):
    queryset = ProfitAndLossAccount.objects.all()
    serializer_class = ProfitAndLossAccountSerializer

class BalanceSheetViewSet(viewsets.ModelViewSet):
    queryset = BalanceSheet.objects.all()
    serializer_class = BalanceSheetSerializer