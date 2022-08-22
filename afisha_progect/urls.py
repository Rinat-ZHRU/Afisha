from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('/admin/', admin.site.urls),
    path('/afisha/', include('afisha_app.urls')),
]
