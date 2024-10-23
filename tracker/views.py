from rest_framework import generics
from .models import Income, Expense, Category
from .serializers import IncomeSerializer, ExpenseSerializer, CategorySerializer

class IncomeListCreate(generics.ListCreateAPIView):
    queryset = Expense.objects.all()
    serializer_class = IncomeSerializer

class ExpenseListCreate(generics.ListCreateAPIView):
    queryset = Expense.objects.all()
    serializer_class = ExpenseSerializer

class CategoryListCreate(generics.ListAPIView):
    queryset = Expense.objects.all()
    serializer_class = IncomeSerializer