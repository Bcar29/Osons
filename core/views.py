from django.shortcuts import render, get_object_or_404
from .models import Article, Projet, Equipe, Federation, Theme, CategorieEquipe, RegionAdministrative

def index(request):
    articles_recents = Article.objects.all()[:6]
    president = Equipe.objects.filter(poste__title='Président').first()
    return render(request, 'core/index.html', {
        'articles_recents': articles_recents,
        'president': president,
    })

def mission(request):
    return render(request, 'core/mission.html')

def president(request):
    return render(request, 'core/president.html')

def articles(request):
    theme_id = request.GET.get('theme')
    if theme_id:
        articles = Article.objects.filter(theme_id=theme_id)
    else:
        articles = Article.objects.all()
    themes = Theme.objects.filter(status=True)
    return render(request, 'core/articles.html', {
        'articles': articles,
        'themes': themes,
    })

def article_detail(request, pk):
    article = get_object_or_404(Article, pk=pk)
    articles_similaires = Article.objects.filter(
        theme=article.theme
    ).exclude(pk=pk)[:2]
    return render(request, 'core/article-detail.html', {
        'article': article,
        'articles_similaires': articles_similaires,
    })

def equipe(request):
    categories = CategorieEquipe.objects.filter(status=True)
    equipe_members = {}
    for categorie in categories:
        equipe_members[categorie] = Equipe.objects.filter(
            categorie=categorie
        )
    return render(request, 'core/equipe.html', {
        'equipe_members': equipe_members,
    })

def federations(request):
    regions = RegionAdministrative.objects.all()
    federations_by_region = {}
    for region in regions:
        federations_by_region[region] = Federation.objects.filter(
            region=region
        )
    return render(request, 'core/federations.html', {
        'federations_by_region': federations_by_region,
    })

def adhesion(request):
    if request.method == 'POST':
        # Traiter le formulaire d'adhésion
        # Créer une instance du modèle avec les données
        pass
    return render(request, 'core/adhesion.html')

def instances(request):
    return render(request, 'core/instances.html')

def initiatives(request):
    return render(request, 'core/initiatives.html')

def projet(request):
    projets = Projet.objects.all()
    return render(request, 'core/porjets.html')