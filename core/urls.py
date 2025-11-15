from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('president/', views.president, name='president'),
    path('articles/', views.articles, name='articles'),
    # path('article/<int:pk>/', views.article_detail, name='article_detail'),
    path('equipe/', views.equipe, name='equipe'),
    # path('membre/<int:pk>/', views.membre_detail, name='membre_detail'),
    path('federations/', views.federations, name='federations'),
    path('adhesion/', views.adhesion, name='adhesion'),
    path('mission/', views.mission, name='mission'),
    path('initiatives/', views.initiatives, name='initiatives'),
    path('instance/', views.instances, name='instance'),
    path('contact/', views.contact, name='contact'),
]