from rest_framework import serializers
from .models import DayBook, LedgerMaster, Ledger, CashBook

class LedgerMasterSerializer(serializers.ModelSerializer):
    class Meta:
        model = LedgerMaster
        fields = [
            'name'
        ]


class LedgerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ledger
        fields = [
            'ledger_name',
            'particulars',
            'amount',
            'active',
            'created_at',
            'updated_at',
        ]


class DayBookSerializer(serializers.ModelSerializer):
    class Meta:
        model = DayBook
        fields = '__all__'

class CashBookSerializer(serializers.ModelSerializer):
    class Meta:
        model = CashBook
        fields = '__all__'


