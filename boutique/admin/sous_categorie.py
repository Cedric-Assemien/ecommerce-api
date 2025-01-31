from django.contrib import admin
from boutique.models.sous_categorie import SousCategorieModel



@admin.register(SousCategorieModel)
class SousCategorieModelAdmin(admin.ModelAdmin):
    list_display = ('nom', 'decsription', 'categorie_id', 'active', 'created_at', 'updated_at')
    search_fields = ('nom', 'categorie_id__nom')
    fields = ('nom', 'decsription', 'categorie_id', 'active')