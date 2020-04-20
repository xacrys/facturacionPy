from django.db import models

from django.contrib.auth.models import User

# Create your models here.


class Generico(models.Model):
    estado = models.BooleanField(default=True)
    fcreado = models.DateTimeField(auto_now_add=True)
    fmodificado = models.DateTimeField(auto_now=True)
    ucreado  = models.ForeignKey(User, on_delete=models.CASCADE)
    umodificado = models.IntegerField(blank=True, null=True)


    class Meta:
        abstract=True