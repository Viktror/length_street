from django.contrib import admin
from .models import *


class CityAdmin(admin.ModelAdmin):
    list_display = ('name',)


admin.site.register(City, CityAdmin)
admin.site.register(Street)
