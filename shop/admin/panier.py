from django.contrib import admin
from shop.models.panier import PanierModel


@admin.register(PanierModel)
class PanierModelAdmin(admin.ModelAdmin):
    list_display = ('reference', 'user_id', 'total', 'active', 'created_at', 'updated_at')
    search_fields = ('reference', 'user_id__username')
    fields = ('reference', 'user_id', 'active')