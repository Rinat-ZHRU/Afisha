from django.db import models


class Category(models.Model):
    """Категории"""
    category_name = models.CharField('Категория', max_length=50)
    cat_description = models.CharField('Краткое описание', max_length=255, null=True, blank=True)

    class Meta:
            verbose_name = 'Категория'
            verbose_name_plural = 'Категории'

    def clean(self):
           self.category_name = self.category_name.capitalize()  # исправление букв на первую заглавную

    def __str__(self):
           return self.category_name


class Genre(models.Model):
    """Жанры"""
    name = models.CharField('Жанр', max_length=255, null=True, blank=True)

    class Meta:
            verbose_name = 'Жанр'
            verbose_name_plural = 'Жанры'

    def clean(self):
           self.name = self.name.capitalize()  # исправление букв на первую заглавную

    def __str__(self):
           return self.name


class Chapter(models.Model):
    """Общий класс Раздел, выборка по категориям"""
    name = models.CharField('Название', max_length=100)
    premiere = models.CharField('Премьера', max_length=50, null=True, blank=True)
    description = models.TextField('Описание', null=True, blank=True)
    address = models.CharField('Место проведения, Адрес', max_length=250)
    date = models.DateTimeField('Дата и время проведения')
    price = models.DecimalField('Цена', max_digits=8, decimal_places=0, null=True, blank=True)
    contacts = models.CharField('Контакты', max_length=250, null=True, blank=True)
    website = models.URLField('Сайт', null=True, blank=True)
    image = models.ImageField('Фото', null=True, blank=True)
    category = models.ForeignKey(Category, verbose_name='Категория', on_delete=models.CASCADE)
    genre = models.ForeignKey(Genre, verbose_name='Жанр', on_delete=models.CASCADE)

    class Meta:
            ordering = ['name']
            verbose_name = 'Раздел'
            verbose_name_plural = 'Разделы'

    def __str__(self):
           return self.name

