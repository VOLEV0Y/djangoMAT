from django.forms import ModelForm
from .models import *

class CategoryForm(ModelForm):
    class Meta:
        model = Category
        fields = ['name']


class ExpenseForm(ModelForm):
    class Meta:
        model = Expense
        fields = ['category', 'amount', 'date']


class ExpenseTagForm(ModelForm):
    class Meta:
        model = ExpenseTag
        fields = ['expense', 'tag_name']