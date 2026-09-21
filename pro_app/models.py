from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    name = models.CharField(max_length=150)

class Expense(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField()

class ExpenseTag(models.Model):
    expense = models.ForeignKey(Expense, on_delete=models.CASCADE)
    tag_name = models.CharField(max_length=50)