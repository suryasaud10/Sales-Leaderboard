
from rest_framework import serializers
from .models import SalesRecord

class SalesRecordSerializer(serializers.ModelSerializer):   
    class Meta:
        model = SalesRecord
        fields = ['id', 'agent_name', 'sales_amount', 'deals_count']

    def validate_sales_amount(self, value):
        if value < 0:
            raise serializers.ValidationError("Sales amount must be a positive number.")
        return value
    
    def validate_deals_count(self, value):
        if value < 0:
            raise serializers.ValidationError("Deals count must be a positive integer.")
        return value
    

class LeaderboardItemSerializer(serializers.Serializer):
    rank = serializers.IntegerField()
    agent_name = serializers.CharField(max_length=100)
    total_sales = serializers.DecimalField(max_digits=10, decimal_places=2)
    total_deals = serializers.IntegerField()