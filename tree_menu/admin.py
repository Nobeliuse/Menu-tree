from django.contrib import admin
from .models import Menu


class MenuAdmin(admin.ModelAdmin):
	list_display = ('id', 'name')
	prepopulated_fields = {'slug': ('name', )}


admin.site.register(Menu, MenuAdmin)