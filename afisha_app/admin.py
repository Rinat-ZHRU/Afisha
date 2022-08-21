from django.contrib import admin
from modeltranslation.admin import TranslationAdmin
from afisha_app.models import Chapter, Category, Genre


@admin.register(Category)
class CategoryAdmin(TranslationAdmin):
    fields = ('category_name', 'cat_description')


@admin.register(Genre)
class GenreAdmin(TranslationAdmin):
    fields = ('name',)


@admin.register(Chapter)
class ChapterAdmin(TranslationAdmin):
    fields = ('name', 'premiere', 'description', 'address',
              'date', 'price', 'contacts', 'website', 'image', 'category', 'genre')




