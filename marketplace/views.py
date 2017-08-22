from django.shortcuts import render,redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Clothes
from .forms import ClothesForm

def clothes_list(request):
    clothes = Clothes.objects.filter(is_published=True).order_by('type')
    return render(request, 'marketplace/clothes_list.html', {'Clothes': Clothes})


def clothes_draft_list(request):
    clothes = Clothes.objects.filter(is_published=False).order_by('type')
    return render(request, 'marketplace/clothes_list.html', {'Clothes': Clothes})
