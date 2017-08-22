from django import forms
from .models import Product

class ClothesForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = ('name', 'type', 'price', 'for_whom', 'picture', 'description', 'count')
