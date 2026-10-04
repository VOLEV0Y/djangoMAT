from django.shortcuts import get_object_or_404
from django.views import View
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.forms.models import model_to_dict
from json import loads

from .models import Category, Expense, ExpenseTag
from .forms import CategoryForm, ExpenseForm, ExpenseTagForm


def _parse_body(request):
    return loads(request.body) if request.body else {}


def _form_response(form, success_message, status=201):
    if form.is_valid():
        obj = form.save()
        return JsonResponse(
            {'status': 'success', 'message': success_message, 'id': obj.pk},
            status=status,
        )
    return JsonResponse(
        {'status': 'error', 'code': 400, 'errors': form.errors},
        status=400,
    )


def _patch_instance(instance, data, form_class):
    full_data = model_to_dict(instance)
    full_data.update(data)
    return form_class(full_data, instance=instance)


def _delete_instance(model, id):
    instance = get_object_or_404(model, id=id)
    instance.delete()
    return JsonResponse({'status': 'success', 'message': 'Deleted!'}, status=200)


@method_decorator(csrf_exempt, 'dispatch')
class CategoryView(View):
    def get(self, request):
        categories = list(Category.objects.values('id', 'name'))
        return JsonResponse({'data': categories})

    def post(self, request):
        form = CategoryForm(_parse_body(request))
        return _form_response(form, 'Added!', status=201)


@method_decorator(csrf_exempt, 'dispatch')
class Get_Categorie(View):
    def get(self, request, id):
        category = get_object_or_404(Category, id=id)
        return JsonResponse({'id': category.id, 'name': category.name})

    def put(self, request, id):
        instance = get_object_or_404(Category, id=id)
        form = CategoryForm(_parse_body(request), instance=instance)
        return _form_response(form, 'Changed!', status=200)

    def patch(self, request, id):
        instance = get_object_or_404(Category, id=id)
        form = _patch_instance(instance, _parse_body(request), CategoryForm)
        return _form_response(form, 'Patched!', status=200)

    def delete(self, request, id):
        return _delete_instance(Category, id)


@method_decorator(csrf_exempt, 'dispatch')
class Post_Expense(View):
    def get(self, request):
        expenses = list(
            Expense.objects.values('id', 'category_id', 'amount', 'date')
        )
        return JsonResponse({'data': expenses})

    def post(self, request):
        form = ExpenseForm(_parse_body(request))
        return _form_response(form, 'Added!', status=201)


@method_decorator(csrf_exempt, 'dispatch')
class Get_Expense(View):
    def get(self, request, id):
        expense = get_object_or_404(Expense, id=id)
        return JsonResponse({
            'id': expense.id,
            'category_id': expense.category_id,
            'amount': str(expense.amount),
            'date': expense.date.isoformat(),
        })

    def put(self, request, id):
        instance = get_object_or_404(Expense, id=id)
        form = ExpenseForm(_parse_body(request), instance=instance)
        return _form_response(form, 'Changed!', status=200)

    def patch(self, request, id):
        instance = get_object_or_404(Expense, id=id)
        form = _patch_instance(instance, _parse_body(request), ExpenseForm)
        return _form_response(form, 'Patched!', status=200)

    def delete(self, request, id):
        return _delete_instance(Expense, id)


@method_decorator(csrf_exempt, 'dispatch')
class Post_ExpenseTag(View):
    def get(self, request):
        tags = list(ExpenseTag.objects.values('id', 'expense_id', 'tag_name'))
        return JsonResponse({'data': tags})

    def post(self, request):
        form = ExpenseTagForm(_parse_body(request))
        return _form_response(form, 'Added!', status=201)


@method_decorator(csrf_exempt, 'dispatch')
class Get_ExpenseTag(View):
    def get(self, request, id):
        tag = get_object_or_404(ExpenseTag, id=id)
        return JsonResponse({
            'id': tag.id,
            'expense_id': tag.expense_id,
            'tag_name': tag.tag_name,
        })

    def put(self, request, id):
        instance = get_object_or_404(ExpenseTag, id=id)
        form = ExpenseTagForm(_parse_body(request), instance=instance)
        return _form_response(form, 'Changed!', status=200)

    def patch(self, request, id):
        instance = get_object_or_404(ExpenseTag, id=id)
        form = _patch_instance(instance, _parse_body(request), ExpenseTagForm)
        return _form_response(form, 'Patched!', status=200)

    def delete(self, request, id):
        return _delete_instance(ExpenseTag, id)