from django.contrib import admin
from customer.models.adresse_de_livraison import AdresseModel


@admin.register(AdresseModel)
class AdresseModelAdmin(admin.ModelAdmin):
    list_display = ('ville', 'quartier', 'rue', 'longitude', 'latitude', 'user_id', 'active', 'created_at', 'updated_at')
    search_fields = ('ville', 'quartier', 'user_id__username')
    fields = ('ville', 'quartier', 'rue', 'longitude', 'latitude', 'indication', 'user_id', 'active')