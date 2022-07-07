from django.db import models


class Post(models.Model):
    nombre = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    asunto = models.CharField(max_length=100)
    createat = models.DateTimeField(auto_now_add=True)
    comentario = models.TextField()
    updateat = models.DateTimeField(auto_now=True)
