from rest_framework import serializers
from .models import Symbols_Transactions,Symbols

class SymbolIDSerializer(serializers.ModelSerializer):
    class Meta:
        model = Symbols
        fields="__all__"


class SymbolTransactionsSerializer(serializers.ModelSerializer):
    class Meta:
        model=Symbols_Transactions
        fields='__all__'