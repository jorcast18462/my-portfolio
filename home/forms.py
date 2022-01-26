from django import forms
from django.db.models import fields
from django.forms import ModelForm

from .models import Post, Tag

class PostForm(ModelForm):

    class Meta:
        model = Post
        fields = '__all__'

        widgets = {
            'tag': forms.CheckboxSelectMultiple(),
        }