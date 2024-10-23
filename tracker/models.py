from django.db import models
from django.contrib.auth.models import User # This lets us associate incomes/expenses with users
class Category(models.Model):
    name = models.CharField(max_length = 255)
    
    def __str__(self):
        return self.name

class Income(models.Models):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null = True)
    description = models.TextField(blank=True, null = True) #Optional description
    date = models.DateField()
    
    def __str__(self):
        return f'{self.amount} - {self.category}'
    
class Expense(models.Models):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null = True)
    description = models.TextField(blank=True, null = True) #Optional description
    date = models.DateField()
    
    def __str__(self):
        return f'{self.amount} - {self.category}'
