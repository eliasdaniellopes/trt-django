from django.db import models


class Registros_filtrados(models.Model):
    titulo = models.CharField(max_length=100)
    linkMag = models.CharField(max_length=1000)
    
    
        