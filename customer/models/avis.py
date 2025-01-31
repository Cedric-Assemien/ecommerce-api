from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class AvisModel(models.Model):

    class Meta:
        verbose_name = "Adresse de Livraison"
        verbose_name_plural = "Adresses de Livraison"

    titre = models.CharField(max_length=254, verbose_name="Titre")
    commentaire = models.TextField()

    user_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_avis_ids")
    produit_id = models.ForeignKey('boutique.ProduitModel', verbose_name="Produit", on_delete=models.CASCADE, related_name="avis_produit_ids")

    active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Date de création")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Date de dernière modification")

    def __str__(self):
        
        return self.titre
        