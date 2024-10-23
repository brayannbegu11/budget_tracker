from rest_framework import serializers
from .models import Income, Expense, Category

class CategorySerializer(serializers.ModelSerializer):
    class meta:
        model = Category
        fields = '__all__'

class IncomeSerializer(serializers.ModelSerializer):
    class meta:
        model = Income
        fields = '__all__'

class ExpenseSerializer(serializers.ModelSerializer):
    class meta:
        model = Expense
        fields = '__all__'