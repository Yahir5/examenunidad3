from django.db import models

# Create your models here.
class nombre(models.Model):
	titulo = models.CharField(max_length=30)
	contenido = models.CharField(max_length=60)
	fecha = models.DateField()