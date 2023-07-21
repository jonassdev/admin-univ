
from django.contrib import admin
from django.urls import path, include
from aplicaciones.academico import views, urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include(urls.urlpatterns)),
]
