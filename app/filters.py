import django_filters

from app.models import Company


class CompanyFilter(django_filters.FilterSet):
    min_cost = django_filters.NumberFilter(field_name='companyproduct__cost', lookup_expr='gte')
    max_cost = django_filters.NumberFilter(field_name='companyproduct__cost', lookup_expr='lte')

    class Meta:
        model = Company
        fields = ('districts', 'products__category', 'name', 'products__name', 'min_cost', 'max_cost')
