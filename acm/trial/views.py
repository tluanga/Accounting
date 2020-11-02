from django.shortcuts import render
from rest_framework import viewsets
from .models import TrialBalance
from .serializers import TrialBalanceSerializer

class TrialBalanceViewSet(viewsets.ModelViewSet):
    queryset = TrialBalance.objects.all()
    serializer_class = TrialBalanceSerializer


