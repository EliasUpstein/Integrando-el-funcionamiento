from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

from Clientes.models import Cliente



class Usuario(AbstractUser):
    clave = models.CharField(verbose_name = "Clave", max_length=4)
    telefono = models.IntegerField(verbose_name = "Telefono", blank=True, null=True) ##Se debera mejorar la especificidad posteriormente, quizas desde el form de creacion de clientes.
    customer = models.OneToOneField(Cliente, verbose_name = "Cliente", on_delete=models.CASCADE, blank=True, null=True)
    

    # Ver ejemplo extendido: https://docs.djangoproject.com/en/4.1/topics/auth/customizing/#auth-custom-user
    