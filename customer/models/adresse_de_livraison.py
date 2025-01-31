from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class AdresseModel(models.Model):

    class Meta:
        verbose_name = "Adresse de Livraison"
        verbose_name_plural = "Adresses de Livraison"

    ville = models.CharField(max_length=254, verbose_name="Ville")
    quartier = models.CharField(max_length=254, verbose_name="Quartier")
    rue = models.CharField(max_length=254, verbose_name="Rue")
    longitude = models.CharField(max_length=20, verbose_name="Longitude")
    latitude = models.CharField(max_length=20, verbose_name="Latitude")
    indication = models.TextField()

    user_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_adresse_ids")

    active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Date de création")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Date de dernière modification")

    def __str__(self):
        
        adresse_complete = '%s, %s' % (self.ville, self.quartier)
        return adresse_complete.strip()
        