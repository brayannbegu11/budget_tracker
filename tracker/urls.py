from django.urls import path
from .views import IncomeListCreate, ExpenseListCreate, CategoryListCreate

urlpatterns = [
    path('income/', IncomeListCreate.as_view(), name='income-list-create'),
    path('expenses/', ExpenseListCreate.as_view(), name='expense-list-create'),
    path('categories/', CategoryListCreate.as_view(), name='category-list-create'),
]