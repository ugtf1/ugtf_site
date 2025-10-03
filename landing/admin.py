from django.contrib import admin
from .models import ScopingCall, BriefMessage, ContactMessage, MailingListSubscriber

@admin.register(ScopingCall)
class ScopingCallAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "phone", "preferred_contact_method", "created_at")
    search_fields = ("name", "email", "phone")

@admin.register(BriefMessage)
class BriefMessageAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "created_at")
    search_fields = ("name", "email")

@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ("email", "phone", "subscribe", "created_at")
    search_fields = ("email", "phone")

@admin.register(MailingListSubscriber)
class MailingListSubscriberAdmin(admin.ModelAdmin):
    list_display = ("email", "created_at")
    search_fields = ("email",)