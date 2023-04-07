from django.db import models
from django.urls import reverse

class MenuLevel01(models.Model):
    name = models.CharField(max_length=50, db_index=True, verbose_name='Название')
    slug = models.SlugField(max_length=50, unique=True, db_index=True,verbose_name='URL')

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Основное Меню'
        verbose_name_plural = 'Основное Меню'

    def get_absolute_url(self):
        return reverse('menu_01', kwargs={'slug_01': self.slug})   

class MenuLevel02(models.Model):
    name = models.CharField(max_length=50, db_index=True, verbose_name='Название')
    slug = models.SlugField(max_length=50, unique=True, db_index=True,verbose_name='URL')
    cat = models.ForeignKey(MenuLevel01,on_delete=models.PROTECT,verbose_name='Категория меню')

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Меню 2 уровня'
        verbose_name_plural = 'Меню 2 уровня'

    def get_absolute_url(self):
        return reverse('menu_02', kwargs={'slug_02': self.slug,'slug_01': self.cat.slug})   

class MenuLevel03(models.Model):
    name = models.CharField(max_length=50, db_index=True, verbose_name='Название')
    slug = models.SlugField(max_length=50, unique=True, db_index=True,verbose_name='URL')
    cat = models.ForeignKey(MenuLevel02,on_delete=models.PROTECT,verbose_name='Категория меню')

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Меню 3 уровня'
        verbose_name_plural = 'Меню 3 уровня'

    def get_absolute_url(self):
        return reverse('menu_03', kwargs={'slug_03': self.slug,'slug_02': self.cat.slug,'slug_01': self.cat.cat.slug})   