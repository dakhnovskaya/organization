from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets

from app.filters import CompanyFilter
from app.models import Product, Company
from app.serializers import ProductSerializer, CompanySerializer


class ProductViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class CompanyViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_class = CompanyFilter
