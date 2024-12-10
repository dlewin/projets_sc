from django.db import models

class Yuze(models.Model):
    LIEU_CHOICES = [
        ('Bungalow', 'Bungalow'),
        ('Zone de tests', 'Zone de tests'),
        ('Prestataire', 'Prestataire'),
        ('Inconnu', 'Inconnu'),
    ]

    ETAT_CHOICES = [
        ('Neuf', 'Neuf'),
        ('En test', 'En test'),
        ('En maintenance', 'En maintenance'),
        ('Défectueux', 'Défectueux'),
        ('NC', 'NC'),
    ]

    ENVIRONNEMENT_CHOICES = [
        ('QA', 'QA'),
        ('Prod', 'Prod'),
        ('Dev', 'Dev'),
        ('Tests', 'Tests'),
        ('NC', 'NC'),
    ]

    CONFIG_HW_CHOICES = [
        ('CM3+', 'CM3+'),
        ('CM4S', 'CM4S'),
    ]

    id_yuze = models.CharField(max_length=100, unique=True)
    lieu = models.CharField(max_length=20, choices=LIEU_CHOICES)
    etat = models.CharField(max_length=20, choices=ETAT_CHOICES)
    version_sw = models.CharField(max_length=20)
    environnement = models.CharField(max_length=10, choices=ENVIRONNEMENT_CHOICES)
    version_hw = models.CharField(max_length=10)
    config_hw = models.CharField(max_length=10, choices=CONFIG_HW_CHOICES)
    flashe = models.BooleanField()
    commentaire = models.TextField(blank=True)

    def __str__(self):
        return self.id_yuze