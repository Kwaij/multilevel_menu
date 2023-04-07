# Generated by Django 4.1.6 on 2023-04-06 18:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menulevel01',
            name='name',
            field=models.CharField(db_index=True, max_length=50, verbose_name='Название'),
        ),
        migrations.AlterField(
            model_name='menulevel01',
            name='slug',
            field=models.SlugField(unique=True, verbose_name='URL'),
        ),
        migrations.AlterField(
            model_name='menulevel02',
            name='name',
            field=models.CharField(db_index=True, max_length=50, verbose_name='Название'),
        ),
        migrations.AlterField(
            model_name='menulevel02',
            name='slug',
            field=models.SlugField(unique=True, verbose_name='URL'),
        ),
        migrations.AlterField(
            model_name='menulevel03',
            name='name',
            field=models.CharField(db_index=True, max_length=50, verbose_name='Название'),
        ),
        migrations.AlterField(
            model_name='menulevel03',
            name='slug',
            field=models.SlugField(unique=True, verbose_name='URL'),
        ),
    ]
