from django import forms
from .models import Respon, Like





class Search(forms.Form):
    search = forms.CharField(max_length=100)

# class ResponForm(forms.ModelForm):
#     class Meta:
#         model = Respon
#         fields = '__all__'

# class LikeForm(forms.ModelForm):
#     class Meta:
#         model = Like
#         fields = '__all__'