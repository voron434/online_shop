from django.shortcuts import render,redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Product
from .forms import ProductForm

def product_list(request):
    products = Product.objects.filter(is_published=True).order_by('type')
    return render(request, 'shop/product_list.html', {'products': products})


def product_draft_list(request):
    products = Product.objects.filter(is_published=False).order_by('type')
    return render(request, 'shop/product_draft_list.html', {'products': products})
