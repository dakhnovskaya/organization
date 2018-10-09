from rest_framework import serializers

from app.models import Product, Category, Company, District, EnterpriseNetwork


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'name')


class ProductSerializer(serializers.ModelSerializer):
    category = CategorySerializer()

    class Meta:
        model = Product
        fields = ('id', 'name', 'category')


class DistrictSerializer(serializers.ModelSerializer):
    class Meta:
        model = District
        fields = ('id', 'name')


class EnterpriseNetworkSerializer(serializers.ModelSerializer):
    class Meta:
        model = EnterpriseNetwork
        fields = ('id', 'name')


class CompanySerializer(serializers.ModelSerializer):
    enterprise_network = EnterpriseNetworkSerializer()
    districts = DistrictSerializer(many=True)
    products = ProductSerializer(many=True)

    class Meta:
        model = Company
        fields = ('id', 'name', 'description', 'enterprise_network', 'districts', 'products')
