from django.contrib import admin
from . models import Code


class CodeAdmin(admin.ModelAdmin):
    list_display = ['name']


admin.site.register(Code, CodeAdmin)
