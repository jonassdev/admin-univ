from django.contrib import admin
from .models import Curso
# Register your models here.


@admin.register(Curso)
class CursoAdmin(admin.ModelAdmin):
    list_display = ('codigo', 'nombre' , 'creditos')
    search_fields = ('nombre' , 'codigo')
    list_filter = ('creditos',)
    list_per_page = 4
    



