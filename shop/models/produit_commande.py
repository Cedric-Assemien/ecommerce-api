from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class ProduitCommandeModel(models.Model):

    class Meta:
        verbose_name = "Produit commandé"
        verbose_name_plural = "Produits commandés"

    produit_id = models.ForeignKey('boutique.ProduitModel', verbose_name="Produit", on_delete=models.CASCADE, related_name="commande_produit_ids")
    commande_id = models.ForeignKey('shop.CommandeModel', on_delete=models.CASCADE, related_name="produit_commande_ids")
    quantite = models.IntegerField()

    active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Date de création")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Date de dernière modification")

    def __str__(self):
        
        return self.commande_id.reference
    
    
    @property
    def total_ligne(self):
        
        return self.produit_id.prix * self.quantite

        