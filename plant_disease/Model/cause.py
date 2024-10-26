# models.py
from django.db import models

class CauseMaladie(models.Model):
    nom = models.CharField(max_length=100)
    description = models.TextField()
    type = models.CharField(max_length=100)  # e.g., "bactérienne", "fongique", "virale", etc.

    def __str__(self):
        return self.nom
