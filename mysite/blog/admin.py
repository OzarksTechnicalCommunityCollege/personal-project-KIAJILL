from django.contrib import admin
from .models import Horse

# Register your models here.
@admin.register(Horse)
class HorseAdmin(admin.ModelAdmin):
    list_display = ['name', 'breed', 'origin', 'color']
    list_filter = ['breed', 'origin', 'color']
    search_fields = ['name', 'breed', 'origin', 'color']

