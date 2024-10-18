from django.db import models
from plant_disease.Model.plant import Plante

class Pest(models.Model):
    nom = models.CharField(max_length=100)
    type = models.CharField(max_length=50)  
    description = models.TextField()
    image = models.ImageField(upload_to='images/pests/', blank=True, null=True)
    plantes = models.ManyToManyField(Plante, related_name='pests')  
    def __str__(self):
        return self.nom
