from django.contrib import admin
from .models import Guest
from import_export.admin import ExportActionMixin
from django.utils.html import format_html

class GuestAdmin(ExportActionMixin, admin.ModelAdmin):
    list_display = ("id","fullname","phone","email","origin","click_to_wa")
    def click_to_wa(self,obj):
        wa_link = "https://wa.me/"
        wa_phone = obj.phone.replace("0","62",1)
        return format_html(f"<a target='_blank' href='{wa_link + wa_phone}'>{obj.phone}</a>")



admin.site.register(Guest, GuestAdmin)

