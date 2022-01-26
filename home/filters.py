from django import forms
from django.db.models import fields
from django.db.models.query import QuerySet
from django.forms import widgets
import django_filters
from django_filters import CharFilter
from django import forms

from .models import *

class PostFilter(django_filters.FilterSet):
    headline = CharFilter(field_name='headline', lookup_expr='icontains', label='Search about')
    tag = django_filters.ModelMultipleChoiceFilter(queryset=Tag.objects.all(),
        widget=forms.CheckboxSelectMultiple, label='Tags')
    class Meta:
        model = Post
        fields = ['headline', 'tag']

        