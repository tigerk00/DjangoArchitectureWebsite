from django.contrib import admin
from .models import ContactInfo, ContactEmail


@admin.register(ContactEmail)
class ContactInfoAdmin(admin.ModelAdmin):
    view_on_site = False
    list_display = ('name', "email", "message")
    list_filter = ("name", "email")
    readonly_fields = ('name', "email", "message")


@admin.register(ContactInfo)
class ContactInfoAdmin(admin.ModelAdmin):
    view_on_site = False
    list_display = ("address", "phone_number", "email_address")
    list_filter = ("phone_number",)



