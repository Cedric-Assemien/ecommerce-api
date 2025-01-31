from django.contrib import admin
from shop.models.produit_commande import ProduitCommandeModel


@admin.register(ProduitCommandeModel)
class ProduitCommandeModelAdmin(admin.ModelAdmin):
    list_display = ('produit_id', 'commande_id', 'quantite', 'total_ligne', 'active', 'created_at', 'updated_at')
    search_fields = ('produit_id__nom', 'commande_id__reference')
    fields = ('produit_id', 'commande_id', 'quantite', 'active')