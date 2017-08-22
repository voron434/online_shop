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


def clothes_new(request):
    if request.method == "POST":
        form = ClothesForm(request.POST)
        if form.is_valid():
            clothes = form.save(commit=False)
            clothes.author = request.user
            clothes.save()
            return redirect('clothes_detail', pk=clothes.pk)
    else:
        form = ClothesForm()
    return render(request, 'marketplace/clothes_edit.html', {'form': form})


def clothes_edit(request, pk):
	clothes = get_object_or_404(Clothes, pk=pk)
	if request.method == "POST":
	    form = ClothesForm(request.POST, instance=clothes)
	    if form.is_valid():
	        clothes = form.save(commit=False)
	        clothes.author = request.user
	        clothes.save()
	        return redirect('clothes_detail', pk=clothes.pk)
	else:
	    form = ClothesForm(instance=clothes)
	return render(request, 'marketplace/clothes_edit.html', {'form': form})


def clothes_detail(request, pk):
    clothes = get_object_or_404(Clothes, pk=pk)
    return render(request, 'marketplace/clothes_detail.html', {'clothes': clothes})
