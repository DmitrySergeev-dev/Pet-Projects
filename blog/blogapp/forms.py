from django import forms
from .models import *


class AddPostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = '__all__'



class AddPostTestForm(forms.Form):
    title = forms.CharField(max_length=255, label='Заголовок')
    body = forms.CharField(widget=forms.Textarea(attrs={'cols': 60, 'rows': 10}),label='Содержимое')
    slug = forms.SlugField(max_length=255)
