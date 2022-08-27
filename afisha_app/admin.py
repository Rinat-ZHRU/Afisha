from django.contrib import admin
from modeltranslation.admin import TranslationAdmin
from afisha_app.models import Chapter, Category, Genre


@admin.register(Category)
class CategoryAdmin(TranslationAdmin):
    list_display = ['id', 'category_name_ru', 'category_name_en', 'cat_description_ru', 'cat_description_en']
    fields = ('category_name', 'cat_description')


@admin.register(Genre)
class GenreAdmin(TranslationAdmin):
    list_display = ['id', 'name_ru', 'name_en']
    fields = ('name',)


@admin.register(Chapter)
class ChapterAdmin(TranslationAdmin):
    # для отображения в просмотре
    list_display = ['id', 'name_ru', 'name_en', 'address_ru', 'address_en', 'price', 'contacts', 'website']
    # для отображения при заполнении
    fields = ('name', 'premiere', 'description', 'address',
              'date', 'price', 'contacts', 'website', 'image', 'category', 'genre',)




