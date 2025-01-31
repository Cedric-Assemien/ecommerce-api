from django.contrib import admin
from boutique.models.produit import ProduitModel


@admin.register(ProduitModel)
class ProduitModelAdmin(admin.ModelAdmin):
    list_display = ('nom', 'decsription', 'prix', 'sous_categorie_id', 'active', 'created_at', 'updated_at')
    search_fields = ('nom', 'sous_categorie_id__nom')
    fields = ('nom', 'decsription', 'prix', 'sous_categorie_id', 'tag_ids', 'active')