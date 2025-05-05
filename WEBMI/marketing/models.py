from django.db import models

class Publication(models.Model):
    titre = models.CharField(max_length=200)
    contenu = models.TextField()
    date_publication = models.DateTimeField(auto_now_add=True)
    visuel = models.ImageField(upload_to='visuels/', blank=True, null=True)

    def __str__(self):
        return self.titre

class CalendrierEditorial(models.Model):
    date = models.DateField()
    contenu_prev = models.TextField()

    def __str__(self):
        return f"{self.date} : {self.contenu_prev}"
