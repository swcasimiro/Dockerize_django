from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('test_app.urls')), # Добавляем наше test_app приложение
]
