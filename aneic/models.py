from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models



class Portada(models.Model):
    texto1 = models.TextField()
    texto2 = models.TextField()


    def __str__(self):
        return self.texto1


class Sobre_aneic(models.Model):
    titulo = models.CharField(max_length=200)
    texto = models.TextField()
    mision = models.TextField()
    vision = models.TextField()
    objetivos = models.TextField()



    def __str__(self):
        return self.titulo



class Preguntas_frecuentes(models.Model):
    titulo = models.CharField(max_length=200)
    texto = models.TextField()

    def __str__(self):
        return self.titulo


class Miembro(models.Model):
    foto = models.ImageField(null=True, blank=True)
    nombre = models.CharField(max_length=300)
    cargo = models.CharField(max_length=300)
    link_instagram = models.CharField(max_length=300, default="#")
    link_twitter = models.CharField(max_length=300, default="#")
    link_linkedin = models.CharField(max_length=300, default="#")


    def __str__(self):
        return self.nombre


