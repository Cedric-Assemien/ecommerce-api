from django.contrib import admin
from shop.models.produit_panier import ProduitPanierModel


@admin.register(ProduitPanierModel)
class ProduitPanierModelAdmin(admin.ModelAdmin):
    list_display = ('produit_id', 'panier_id', 'quantite', 'total_ligne', 'active', 'created_at', 'updated_at')
    search_fields = ('produit_id__nom', 'panier_id__reference')
    fields = ('produit_id', 'panier_id', 'quantite', 'active')