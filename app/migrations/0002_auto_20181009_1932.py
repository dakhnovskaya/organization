# Generated by Django 2.1.2 on 2018-10-09 15:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name': 'Категория', 'verbose_name_plural': 'Категории'},
        ),
        migrations.AlterModelOptions(
            name='company',
            options={'verbose_name': 'Предприятие', 'verbose_name_plural': 'Предприятия'},
        ),
        migrations.AlterModelOptions(
            name='district',
            options={'verbose_name': 'Район города', 'verbose_name_plural': 'Районы города'},
        ),
        migrations.AlterModelOptions(
            name='enterprisenetwork',
            options={'verbose_name': 'Сеть предприятий', 'verbose_name_plural': 'Сети предприятий'},
        ),
        migrations.AlterModelOptions(
            name='product',
            options={'verbose_name': 'Услуга\\товар', 'verbose_name_plural': 'Услуги\\товары'},
        ),
        migrations.RemoveField(
            model_name='product',
            name='company',
        ),
        migrations.AddField(
            model_name='company',
            name='product',
            field=models.ManyToManyField(through='app.CompanyProduct', to='app.Product', verbose_name='Предприятие'),
        ),
    ]