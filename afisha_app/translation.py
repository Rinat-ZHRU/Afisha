from modeltranslation.translator import register, TranslationOptions
from afisha_app.models import Chapter, Category, Genre


@register(Chapter)
class ChapterTranslationOptions(TranslationOptions):
    fields = ('name', 'premiere', 'description', 'address')


@register(Category)
class CategoryTranslationOptions(TranslationOptions):
    fields = ('category_name', 'cat_description')


@register(Genre)
class GenreTranslationOptions(TranslationOptions):
    fields = ('name',)