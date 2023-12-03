from django.db import models

# Create your models here.

class Tours(models.Model):
    codigo=models.CharField(primary_key=True,max_length=6)
    circuito=models.CharField(max_length=50)
    descripcion=models.CharField(max_length=50)
    aereo=models.CharField(max_length=50)
    traslados=models.CharField(max_length=50)
    comidas=models.CharField(max_length=50)

    def __str__(self):
        texto="{0} ({1})"
        return texto.format(self.codigo, self.circuito)
