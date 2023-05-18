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


class Service(models.Model):
    title = models.TextField(max_length=100, default='Услуга', verbose_name='Заголовок')
    description = models.TextField(verbose_name='Описание')

    class Meta:
        verbose_name = 'Услуга'
        verbose_name_plural = 'Услуги'

    def __str__(self):
        return self.title


class SubService(models.Model):
    description = models.TextField(verbose_name='Описание')
    service = models.ForeignKey(Service, null=True, on_delete=models.deletion.SET_NULL, related_name='sub_services',
                                verbose_name='Услуга')

    class Meta:
        verbose_name = 'Подуслуга'
        verbose_name_plural = 'Подуслуги'

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


class Contact(models.Model):
    address = models.CharField(max_length=200)
    phones = models.JSONField(default=list)
    emails = models.JSONField(default=list)

    class Meta:
        verbose_name = 'Контакты'
        verbose_name_plural = 'Контакты'

    def __str__(self):
        return self.address
