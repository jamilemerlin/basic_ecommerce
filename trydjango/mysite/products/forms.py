from django import forms
from .models import Product


class ProductForm(forms.ModelForm):
    title = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Your title'}))
    description = forms.CharField(required=False,
                                  widget=forms.Textarea(
                                          attrs={'placeholder': 'Describe your product',
                                                 'rows': 10}
                                  ))
    # email = forms.EmailField()
    price = forms.DecimalField(initial=199.99)
    class Meta:
        model = Product
        fields = [
                'title',
                'description',
                'price'
        ]

class RawProductForm(forms.Form):
    title = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Your title'}))
    description = forms.CharField(required=False,
                                  widget=forms.Textarea(
                                          attrs={'placeholder': 'Describe your product',
                                                 'rows': 10}
                                  ))
    price = forms.DecimalField(initial=199.99)
