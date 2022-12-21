from django_filters import rest_framework as filters
from rest_framework.response import Response
from .models import Todo


class CharFilterInFilter(filters.BaseInFilter,filters.CharFilter):
    pass

class  TodoFilter(filters.FilterSet):
    title=CharFilterInFilter(field_name='title',lookup_expr='in')
    is_completed=CharFilterInFilter(field_name='is_completed',lookup_expr='in')
    
    class Meta:
        model=Todo
        fields=['title','is_completed']
