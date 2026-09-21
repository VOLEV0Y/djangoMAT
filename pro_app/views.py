from django.shortcuts import render
from django.views import View
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page, never_cache
from django.views.generic import TemplateView
from django.shortcuts import get_object_or_404
from django.http import HttpResponse, HttpRequest, JsonResponse
from .models import *
from .forms import *
from json import loads
from django.views.decorators.csrf import csrf_exempt

@method_decorator(csrf_exempt, 'dispatch')
class CategoryView(View):
    def get(self, request):
        categories = list(Category.objects.values('id', 'name'))
        obj = {
            'data': categories
        }
        return JsonResponse(obj)
    
    def post(self, request):
        raw_json = request.body
        new_data = loads(raw_json)
        
        form = CategoryForm(new_data)
        if form.is_valid():
            quote = form.save()
            return JsonResponse(
                {'status': 'success',
                 'message': 'Added!',
                 'id': quote.pk}, status=201
            )
        else:
            return JsonResponse(
                {'status': 'error', 'code': 400},
                status=400
                )

class Get_Categorie(View):
    def get(self, request, id):
        categories = Category.objects.values('id', 'name').get(id=id)
        return JsonResponse(categories)


@method_decorator(csrf_exempt, 'dispatch')
class Post_Expense(View):
    def get(self, request):
        expenses = list(Expense.objects.values('id', 'category_id', 'amount', 'date'))
        obj = {
            'data': expenses
        }
        return JsonResponse(obj)

    def post(self, request):
        raw_json = request.body
        new_data = loads(raw_json)
        
        form = ExpenseForm(new_data)
        if form.is_valid():
            quote = form.save()
            return JsonResponse(
                {'status': 'success',
                 'message': 'Added!',
                 'id': quote.pk}, status=201
            )
        else:
            return JsonResponse(
                {'status': 'error', 'code': 400},
                status=400
                )

@method_decorator(csrf_exempt, 'dispatch')
class Post_ExpenseTag(View):
    def get(self, request, id):
        tag = ExpenseTag.objects.values('id', 'expense_id', 'tag_name').get(id=id)
        return JsonResponse(tag)

    def post(self, request):
        raw_json = request.body
        new_data = loads(raw_json)
        
        form = ExpenseTagForm(new_data)
        if form.is_valid():
            quote = form.save()
            return JsonResponse(
                {'status': 'success',
                 'message': 'Added!',
                 'id': quote.pk}, status=201
            )
        else:
            return JsonResponse(
                {'status': 'error', 'code': 400},
                status=400
                )