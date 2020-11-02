from rest_framework import serializers
from .models import DayBook, Ledger, CashBook

# class LedgerMasterSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = LedgerMaster
#         fields = [
#             'name'
#         ]


class LedgerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ledger
        fields = '__all__'


class DayBookSerializer(serializers.ModelSerializer):
    class Meta:
        model = DayBook
        fields = '__all__'

class CashBookSerializer(serializers.ModelSerializer):
    class Meta:
        model = CashBook
        fields = '__all__'


