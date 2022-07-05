from django.shortcuts import render, get_object_or_404
from .models import (Order,
                     Categories,
                     Supplier)
from django.views import generic
from django.core.paginator import Paginator
from django.db.models import Q
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin


def index(request):
    num_order = Order.objects.all().count()
    num_categories = Categories.objects.all().count()
    num_supplier = Supplier.objects.count()

    num_visits = request.session.get('num_visits', 1)
    request.session['num_visits'] = num_visits + 1

    context = {
        'num_order': num_order,
        'num_categories': num_categories,
        'num_supplier': num_supplier,
        'num_visits': num_visits,
    }
    return render(request, 'index.html', context=context)


def suppliers(request):
    paginator = Paginator(Supplier.objects.all(), 3)
    page_number = request.GET.get('page')
    paged_suppliers = paginator.get_page(page_number)
    my_context = {
        "suppliers": paged_suppliers,
    }
    return render(request, 'suppliers.html', context=my_context)


def supplier(request, supplier_id):
    single_supplier = get_object_or_404(Supplier, pk=supplier_id)
    return render(request, 'supplier.html', context={"supplier": single_supplier})


def info(request):
    return render(request, 'info.html')


def orders(request):
    return render(request, 'orders.html')


def calculations(request):
    return render(request, 'calculations.html')


def contacts(request):
    return render(request, 'contacts.html')


def my_suppliers(request):
    return render(request, 'my_suppliers.html')


def new_items(request):
    return render(request, 'new_items.html')


def invoices(request):
    return render(request, 'invoices.html')
