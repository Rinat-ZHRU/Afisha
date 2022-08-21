from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from afisha_app.models import Chapter, Category, Genre
from afisha_app.serializers import CategorySerializer, ChapterSerializer, GenreSerializer
from rest_framework import viewsets


class CategoryViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Category.objects.all().order_by('id')
    serializer_class = CategorySerializer


class GenreViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Genre.objects.all().order_by('name')
    serializer_class = GenreSerializer


class ChapterViewSet(viewsets.ModelViewSet):
    queryset = Chapter.objects.all().order_by('id')
    serializer_class = ChapterSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['name', 'date', 'category__category_name', 'genre__name']
