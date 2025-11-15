from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.core.mail import EmailMessage
from django.conf import settings
from .models import Article, Equipe, Federation, Theme, CategorieEquipe, RegionAdministrative
from .forms import ContactForm

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

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            contact_message = form.save()
            
            # Envoyer un email à l'email de réception avec tous les détails
            try:
                # Email pour l'organisation avec toutes les informations du formulaire
                subject = f"Nouveau message de contact - {contact_message.sujet}"
                message_body = f"""Nouveau message reçu depuis le formulaire de contact :

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

INFORMATIONS DU CONTACT :
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Prénom : {contact_message.prenom}
Nom : {contact_message.nom}
Email : {contact_message.email}
Téléphone : {contact_message.telephone or 'Non renseigné'}

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

MESSAGE :
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Sujet : {contact_message.sujet}

{contact_message.message}

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Date d'envoi : {contact_message.date_envoi.strftime('%d/%m/%Y à %H:%M')}

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Pour répondre à ce message, répondez simplement à cet email.
L'email sera automatiquement envoyé à : {contact_message.email}
"""
                
                # Utiliser EmailMessage pour permettre le reply-to
                email = EmailMessage(
                    subject=subject,
                    body=message_body,
                    from_email=settings.DEFAULT_FROM_EMAIL,
                    to=[settings.CONTACT_EMAIL],  # Seul l'email de réception reçoit le message
                    reply_to=[contact_message.email],  # Permet de répondre directement à l'utilisateur
                )
                email.send(fail_silently=False)
                
                messages.success(request, 'Votre message a été envoyé avec succès ! Nous vous répondrons dans un bref délai.')
                return redirect('contact')
            except Exception as e:
                # En cas d'erreur d'envoi d'email, on sauvegarde quand même le message
                error_msg = str(e)
                if 'BadCredentials' in error_msg or 'Username and Password not accepted' in error_msg:
                    user_message = (
                        'Votre message a été enregistré avec succès. '
                        'Cependant, une erreur d\'authentification email est survenue. '
                        'Veuillez contacter l\'administrateur pour configurer correctement les paramètres SMTP. '
                        'Votre message sera traité dès que possible.'
                    )
                else:
                    user_message = (
                        f'Votre message a été enregistré avec succès. '
                        f'Une erreur technique est survenue lors de l\'envoi de l\'email. '
                        f'Votre message sera traité dès que possible.'
                    )
                messages.warning(request, user_message)
                # Log l'erreur complète pour le développeur (dans un environnement de production, utilisez logging)
                print(f"Erreur d'envoi d'email: {error_msg}")
                return redirect('contact')
        else:
            messages.error(request, 'Veuillez corriger les erreurs dans le formulaire.')
    else:
        form = ContactForm()
    
    return render(request, 'core/contact.html', {'form': form})