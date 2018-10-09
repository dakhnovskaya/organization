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


class Item(RepresentationFieldNameMixin, models.Model):
    name = models.CharField(max_length=255, verbose_name='Название')
    category = models.ForeignKey(Category, verbose_name='Категория', on_delete=models.PROTECT)


class CompanyLinkDistrict(RepresentationFieldNameMixin, models.Model):
    district = models.ForeignKey(District, verbose_name='Район города', on_delete=models.PROTECT)
    company = models.ForeignKey(Company, verbose_name='Предприятие', on_delete=models.PROTECT)


class ItemLinkCompany(RepresentationFieldNameMixin, models.Model):
    item = models.ForeignKey(Item, verbose_name='Услуга\товар', on_delete=models.PROTECT)
    company = models.ForeignKey(Company, verbose_name='Предприятие', on_delete=models.PROTECT)
    cost = models.FloatField(verbose_name='Цена')
