from django import forms
from .models import Item, Container


class ItemForm(forms.ModelForm):

    container = forms.ModelChoiceField(
        required=False,
        empty_label="None",
        queryset=Container.objects.order_by('-creation_date'))

    class Meta:
        model = Item
        fields = ['name', 'description', 'photo', 'container']

        widgets = {
            'name':
            forms.TextInput(attrs={'class': 'form-control'}),
            'description':
            forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 3
            }),
            'photo':
            forms.FileInput(attrs={'capture': 'camera'}),
        }


class ContainerForm(forms.ModelForm):

    container = forms.ModelChoiceField(
        required=False,
        empty_label="None",
        queryset=Container.objects.order_by('-creation_date'))

    class Meta:
        model = Container
        fields = ['name', 'description', 'photo', 'container']

        widgets = {
            'name':
            forms.TextInput(attrs={'class': 'form-control'}),
            'description':
            forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 3
            }),
            'photo':
            forms.FileInput(attrs={'capture': 'camera'}),
        }
