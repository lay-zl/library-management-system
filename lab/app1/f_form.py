from django import forms
from .models import *


class EditBookForm(forms.ModelForm):
    # bname = forms.CharField(max_length=70)
    # publisher = forms.CharField(max_length=70)
    # auther = forms.CharField(max_length=70)
    class Meta:
        model = Book
        fields = '__all__'



class EditUser(forms.ModelForm):
    class Meta:
        model = User
        fields = '__all__'
