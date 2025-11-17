# core/admin.py
from re import A
from django.contrib import admin

from django.db import models
from .models import Mission, Projet, Theme, Article, Poste, CategorieEquipe, Equipe, Initiative, Instance,RegionAdministrative, Federation

from .models import Mission, ContactMessage


@admin.register(Mission)
class MissionAdmin(admin.ModelAdmin):
    list_display = ('title',)


@admin.register(Theme)
class ThemeAdmin(admin.ModelAdmin):
    list_display = ('title', 'status')

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('author', 'theme', )

@admin.register(Poste)
class PosteAdmin(admin.ModelAdmin):
    list_display = ('title', 'status')

@admin.register(CategorieEquipe)
class CategorieEquipeAdmin(admin.ModelAdmin):
    list_display = ('name', 'status')

@admin.register(Equipe)
class EquipeAdmin(admin.ModelAdmin):
    list_display = ('user', 'first_name', 'last_name')

@admin.register(Instance)
class InstanceAdmin(admin.ModelAdmin):
    list_display = ('title', 'status')

@admin.register(Initiative)
class InitiativeAdmin(admin.ModelAdmin):
    list_display = ('title', 'status')

@admin.register(RegionAdministrative)
class RegionAdministrativeAdmin(admin.ModelAdmin):
    list_display = ('name', )
    
@admin.register(Federation)
class FederationAdmin(admin.ModelAdmin):
    list_display = ('region', 'name')
    
@admin.register(Projet)
class Projet(admin.ModelAdmin):
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

