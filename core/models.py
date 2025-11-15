from django.db import models
from django_summernote.fields import SummernoteTextField
from django.contrib.auth import get_user_model

User = get_user_model()


class Mission(models.Model):
    title = models.CharField(max_length=200, default="")
    content = SummernoteTextField()

    def __str__(self):
       
        return self.title


class Theme(models.Model):
    title = models.CharField(max_length=50)
    description = SummernoteTextField()
    status = models.BooleanField(default=True)

    def __str__(self):
        return self.title


class Article(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    theme = models.ForeignKey(Theme, on_delete=models.CASCADE)
    content = SummernoteTextField()
    video = models.FileField(
        upload_to="core/videos/",  # 🔹 Indique un dossier où les vidéos seront stockées
        null=True,                 # 🔹 Rendre le champ optionnel
        blank=True,                # 🔹 Permet de ne pas toujours téléverser une vidéo
    )

    def __str__(self):
        return f"Article de {self.author.username} - {self.theme.title}"


class Poste(models.Model):
    title = models.CharField(max_length=255)
    description = SummernoteTextField()
    status = models.BooleanField(default=True)

    def __str__(self):
        return self.title

class CategorieEquipe(models.Model):
    name = models.CharField(max_length=50)
    description = SummernoteTextField()
    status = models.BooleanField(default=True)

class Equipe(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    categorie = models.ForeignKey(CategorieEquipe, on_delete=models.CASCADE)
    poste = models.ForeignKey(Poste, on_delete=models.CASCADE, related_name="actuel_poste")
    last_poste = models.ForeignKey(
        Poste,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="ancien_poste",
    )
    bio = SummernoteTextField()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Instance(models.Model):  
    title = models.CharField(max_length=50)
    description = SummernoteTextField()
    status = models.BooleanField(default=True)

    def __str__(self):
        return self.title


class Initiative(models.Model):
    title = models.CharField(max_length=50)
    description = SummernoteTextField()
    status = models.BooleanField(default=True)

    def __str__(self):
        return self.title

class RegionAdministrative(models.Model):
    name = models.CharField(max_length=50)
 
class Federation(models.Model):
    region = models.ForeignKey(RegionAdministrative, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to="core/federation", null=True, blank=True)

    def __str__(self):
        return self.name


class ContactMessage(models.Model):
    nom = models.CharField(max_length=100, verbose_name="Nom")
    prenom = models.CharField(max_length=100, verbose_name="Prénom")
    email = models.EmailField(verbose_name="Email")
    telephone = models.CharField(max_length=20, blank=True, null=True, verbose_name="Téléphone")
    sujet = models.CharField(max_length=200, verbose_name="Sujet")
    message = models.TextField(verbose_name="Message")
    date_envoi = models.DateTimeField(auto_now_add=True, verbose_name="Date d'envoi")
    lu = models.BooleanField(default=False, verbose_name="Lu")
    
    class Meta:
        verbose_name = "Message de contact"
        verbose_name_plural = "Messages de contact"
        ordering = ['-date_envoi']
    
    def __str__(self):
        return f"{self.prenom} {self.nom} - {self.sujet}"