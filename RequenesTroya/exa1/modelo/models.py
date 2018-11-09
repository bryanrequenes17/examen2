from django.db import models

# Create your models here.
class Estudiantes(models.Model):


    listaGenero = (
        ('F', 'Femenino'),
        ('M', 'Masculino'),
    )

    cedula = models.CharField(max_length= 10)
    nombres = models.CharField(max_length= 60)
    apellidos = models.CharField(max_length= 60)
    edad = models.IntegerField(null= True)
    direccion = models.CharField(max_length= 150, null=True)
    genero = models.CharField(max_length= 15, choices= listaGenero, default='Masculino')
    
