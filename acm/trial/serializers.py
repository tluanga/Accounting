from rest_framework import serializers
from .models import TrialBalance

class TrialBalanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = TrialBalance
        fields = '__all__'
        