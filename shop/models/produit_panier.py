from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class ProduitPanierModel(models.Model):

    class Meta:
        verbose_name = "Produit du panier"
        verbose_name_plural = "Produits du panier"

    produit_id = models.ForeignKey('boutique.ProduitModel', verbose_name="Produit", on_delete=models.CASCADE, related_name="panier_produit_ids")
    panier_id = models.ForeignKey('shop.PanierModel', on_delete=models.CASCADE, related_name="produit_panier_ids")
    quantite = models.IntegerField()

    active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Date de création")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Date de dernière modification")

    def __str__(self):
        
        return self.panier_id.reference
    
    
    @property
    def total_ligne(self):
        
        return self.produit_id.prix * self.quantite

        