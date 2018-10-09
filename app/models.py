from django.db import models


class RepresentationFieldNameMixin:
    def __str__(self):
        return self.name


class District(RepresentationFieldNameMixin, models.Model):
    name = models.CharField(max_length=255, verbose_name='Название')

    class Meta:
        verbose_name = 'Район города'
        verbose_name_plural = 'Районы города'


class Category(RepresentationFieldNameMixin, models.Model):
    name = models.CharField(max_length=255, verbose_name='Название')

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class EnterpriseNetwork(RepresentationFieldNameMixin, models.Model):
    name = models.CharField(max_length=255, verbose_name='Название')

    class Meta:
        verbose_name = 'Сеть предприятий'
        verbose_name_plural = 'Сети предприятий'


class Product(RepresentationFieldNameMixin, models.Model):
    name = models.CharField(max_length=255, verbose_name='Название')
    category = models.ForeignKey(Category, verbose_name='Категория', on_delete=models.PROTECT)

    class Meta:
        verbose_name = 'Услуга\товар'
        verbose_name_plural = 'Услуги\товары'


class Company(RepresentationFieldNameMixin, models.Model):
    name = models.CharField(max_length=255, verbose_name='Название')
    description = models.CharField(max_length=500, verbose_name='Описание')
    enterprise_network = models.ForeignKey(EnterpriseNetwork, verbose_name='Сеть предприятий', on_delete=models.PROTECT)
    district = models.ManyToManyField(District, verbose_name='Район города')
    products = models.ManyToManyField(Product, through='CompanyProduct', verbose_name='Предприятие')

    class Meta:
        verbose_name = 'Предприятие'
        verbose_name_plural = 'Предприятия'


class CompanyProduct(models.Model):
    company = models.ForeignKey(Company, verbose_name='Предприятие', on_delete=models.PROTECT)
    product = models.ForeignKey(Product, verbose_name='Услуга\товар', on_delete=models.PROTECT)
    cost = models.FloatField(verbose_name='Цена')

    class Meta:
        verbose_name = 'Услуга\товар предприятия'
        verbose_name_plural = 'Услуги\товары предприятия'
