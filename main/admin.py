from django.contrib import admin
from .models import Guest
from import_export.admin import ExportActionMixin

class GuestAdmin(ExportActionMixin, admin.ModelAdmin):
    list_display = ("id","fullname","phone","email")

admin.site.register(Guest, GuestAdmin)

