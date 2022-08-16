from django.contrib import admin

# Register your models here.
from .models import Cuenta

class ProjectAdmin (admin.ModelAdmin):
    readonly_fields= ('created','updated')
admin.site.register(Cuenta)
