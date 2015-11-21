from django import forms

from .models import List_items1

class PostForm(forms.ModelForm):

    class Meta:
        model = List_items1
        fields = ('title', 'quentity', 'zipcode', 'discription', 'address')
