from django.contrib import admin
from .models import Guest

class GuestAdmin(admin.ModelAdmin):
    list_display = ("id","fullname","phone","email")

admin.site.register(Guest, GuestAdmin)

