from django.db import models

# Create your models here.

class Familiar(models.Model):
    nombre= models.CharField(max_length=50)
    apellido= models.CharField(max_length=50)
    fecha_nacimiento= models.DateField()
    estado_civil=models.CharField(max_length=50)
    email=models.EmailField()
    celular=models.IntegerField()