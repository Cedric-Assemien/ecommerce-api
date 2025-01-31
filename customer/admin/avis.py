from django.contrib import admin
from customer.models.avis import AvisModel


@admin.register(AvisModel)
class AvisModelAdmin(admin.ModelAdmin):
    list_display = ('titre', 'commentaire', 'user_id', 'produit_id', 'active', 'created_at', 'updated_at')
    search_fields = ('titre', 'user_id__username', 'produit_id__nom')
    fields = ('titre', 'commentaire', 'user_id', 'produit_id', 'active')