from django.urls import path
from .views import *

urlpatterns = [
    path('categories/', CategoryView.as_view()),
    path('categorie/<int:id>', Get_Categorie.as_view()),

    path('expense/', Post_Expense.as_view()),
    path('expense/<int:id>', Get_Expense.as_view()),

    path('expense/<int:id>/tag/', Post_ExpenseTag.as_view()),
]