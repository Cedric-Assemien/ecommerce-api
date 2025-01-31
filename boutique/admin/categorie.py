from django.contrib import admin
from boutique.models.categorie import CategorieModel


@admin.register(CategorieModel)
class CategorieModelAdmin(admin.ModelAdmin):
    list_display = ('nom', 'decsription', 'active', 'created_at', 'updated_at')
    search_fields = ('nom',)
    fields = ('nom', 'decsription', 'active')