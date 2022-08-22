from django.urls import path
from afisha_app.views import CategoryViewSet, ChapterViewSet, GenreViewSet


urlpatterns = [
    path('category/', CategoryViewSet.as_view({'get': 'list'}), name='Список категорий'),
    path('genre/', GenreViewSet.as_view({'get': 'list'}), name='Список жанров'),
    path('chapter/', ChapterViewSet.as_view({'get': 'list'}), name='Список разделов'),
    path('chapter/<int:pk>/', ChapterViewSet.as_view({'get': 'retrieve'}), name='Детализация раздела'),
]