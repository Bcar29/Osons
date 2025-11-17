# core/admin.py
from re import A
from django.contrib import admin
from django.db import models
from .models import Mission, Projet, Theme, Article, Poste, CategorieEquipe, Equipe, Initiative, Instance,RegionAdministrative, Federation

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