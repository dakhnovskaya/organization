from django.conf.urls import url
from django.urls import include
from rest_framework import routers

from app import views

router = routers.DefaultRouter()
router.register(r'products', views.ProductViewSet)
router.register(r'organizations', views.CompanyViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
]
