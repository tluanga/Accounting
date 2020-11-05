from rest_framework import serializers
from .models import TradingAccount, ProfitAndLossAccount, BalanceSheet

class TradingAccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = TradingAccount
        fields = '__all__'

class ProfitAndLossAccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProfitAndLossAccount
        fields = '__all__'

class BalanceSheetSerializer(serializers.ModelSerializer):
    class Meta:
        model = BalanceSheet
        fields = '__all__'
