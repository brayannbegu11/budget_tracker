from django.urls import path
from .views import IncomeListCreate, ExpenseListCreate, CategoryListCreate
from .views_auth import LoginView, RegisterView

urlpatterns = [
    path('income/', IncomeListCreate.as_view(), name='income-list-create'),
    path('expenses/', ExpenseListCreate.as_view(), name='expense-list-create'),
    path('categories/', CategoryListCreate.as_view(), name='category-list-create'),
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
]