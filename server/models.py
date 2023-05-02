from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название')
    description = models.TextField(verbose_name='Описание')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Цена')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Запись создана')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Запись изменена')

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'

    def __str__(self):
        return self.name


class Partner(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название')

    class Meta:
        verbose_name = 'Партнер'
        verbose_name_plural = 'Партнеры'

    def __str__(self):
        return self.name


class Direction(models.Model):
    description = models.TextField(verbose_name='Описание')

    class Meta:
        verbose_name = 'Направление деятельности'
        verbose_name_plural = 'Направления деятельности'

    def __str__(self):
        return self.description


class Project(models.Model):
    description = models.TextField(verbose_name='Описание')

    class Meta:
        verbose_name = 'Проект'
        verbose_name_plural = 'Проекты'

    def __str__(self):
        return self.description


class Service(models.Model):
    description = models.TextField(verbose_name='Описание')

    class Meta:
        verbose_name = 'Услуга'
        verbose_name_plural = 'Услуги'

    def __str__(self):
        return self.description


class History(models.Model):
    description = models.TextField(verbose_name='Описание')
    POSITION = (
        ("left", "Слева"),
        ("right", "Справа"),
    )
    status = models.CharField(choices=POSITION, default='Слева', max_length=5, verbose_name='Позиция')
    image_path = models.ImageField(upload_to='history', null=True, blank=True, verbose_name='Изображение')

    class Meta:
        verbose_name = 'История'
        verbose_name_plural = 'Истории'

    def __str__(self):
        return self.description
