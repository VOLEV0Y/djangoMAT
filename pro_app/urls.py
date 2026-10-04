from django.urls import path
from .views import *

urlpatterns = [
    path('categories/', CategoryView.as_view()),
    path('categories/<int:id>', Get_Categorie.as_view()),

    path('expenses/', Post_Expense.as_view()),
    path('expenses/<int:id>', Get_Expense.as_view()),

    path('tags/', Post_ExpenseTag.as_view()),
    path('tags/<int:id>', Get_ExpenseTag.as_view()),
]