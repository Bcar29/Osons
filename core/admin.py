# core/admin.py
from django.contrib import admin
from .models import Mission, ContactMessage

@admin.register(Mission)
class MissionAdmin(admin.ModelAdmin):
    list_display = ('title',)

@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('prenom', 'nom', 'email', 'sujet', 'date_envoi', 'lu')
    list_filter = ('lu', 'date_envoi')
    search_fields = ('nom', 'prenom', 'email', 'sujet', 'message')
    readonly_fields = ('date_envoi',)
    list_editable = ('lu',)
    date_hierarchy = 'date_envoi'
    
    fieldsets = (
        ('Informations personnelles', {
            'fields': ('nom', 'prenom', 'email', 'telephone')
        }),
        ('Message', {
            'fields': ('sujet', 'message')
        }),
        ('Statut', {
            'fields': ('lu', 'date_envoi')
        }),
    )
