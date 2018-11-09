from django.db import models

# Create your models here.
class Usuario(models.Model):

    cedula = models.CharField(max_length=10,unique=True, null=False)
    apellidoPaterno = models.CharField(max_length=70,  null=False)
    apellidoMaterno = models.CharField(max_length=70,  null=False)
    nombres = models.CharField(max_length=70,  null=False)
    Sexo=models.CharField(max_length = 20)
    estado = models.BooleanField(default=True)
