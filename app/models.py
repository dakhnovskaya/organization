from django.db import models


class RepresentationFieldNameMixin:
    def __str__(self):
        return self.name


class District(RepresentationFieldNameMixin, models.Model):
    name = models.CharField(max_length=255, verbose_name='Название')


class Category(RepresentationFieldNameMixin, models.Model):
    name = models.CharField(max_length=255, verbose_name='Название')


class EnterpriseNetwork(RepresentationFieldNameMixin, models.Model):
    name = models.CharField(max_length=255, verbose_name='Название')


class Company(RepresentationFieldNameMixin, models.Model):
    name = models.CharField(max_length=255, verbose_name='Название')
    description = models.CharField(max_length=500, verbose_name='Описание')
    enterprise_network = models.ForeignKey(EnterpriseNetwork, verbose_name='Сеть предприятий', on_delete=models.PROTECT)
    district = models.ManyToManyField(District, verbose_name='Район города')


class Product(RepresentationFieldNameMixin, models.Model):
    name = models.CharField(max_length=255, verbose_name='Название')
    category = models.ForeignKey(Category, verbose_name='Категория', on_delete=models.PROTECT)
    company = models.ManyToManyField(Company, through='CompanyProduct', verbose_name='Предприятие')


class CompanyProduct(RepresentationFieldNameMixin, models.Model):
    company = models.ForeignKey(Company, verbose_name='Предприятие')
    product = models.ForeignKey(Product, verbose_name='Услуга\товар')
    cost = models.FloatField(verbose_name='Цена')

