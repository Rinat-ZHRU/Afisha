from afisha_app.models import Category, Chapter, Genre
from rest_framework import serializers


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'  # все поля


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = '__all__'


class ChapterSerializer(serializers.ModelSerializer):
    # category_name = serializers.SerializerMethodField()
    genre = GenreSerializer()
    category = CategorySerializer()

    class Meta:
        model = Chapter
        fields = ('name', 'premiere', 'description', 'address', 'date', 'price',
                  'contacts', 'website', 'image', 'category', 'genre')
