from django.db import models

# Create your models here.
class Musica(models.Model):
    nome = models.CharField(max_length=100)
    compositor = models.CharField(max_length=100)
    duracao = models.CharField(max_length=10)
    quemSugeriu = models.CharField(max_length=100, default="eu")        
