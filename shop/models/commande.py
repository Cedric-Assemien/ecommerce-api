from django.db import models
from django.contrib.auth import get_user_model
from shop.models.produit_commande import ProduitCommandeModel
User = get_user_model()

class CommandeModel(models.Model):

    class Meta:
        verbose_name = "Commande"
        verbose_name_plural = "Commandes"

    reference = models.CharField(max_length=254, verbose_name="Référence")
    date_de_commande = models.DateTimeField(auto_now_add=True)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_commande_ids")

    active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Date de création")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Date de dernière modification")

    def __str__(self):
        
        return self.reference
    
    @property
    def total(self):
        lignes = ProduitCommandeModel.objects.filter(commande_id=self.id)
        total = 0
        for ligne in lignes:
            total += ligne.total_ligne

        return total