from django.contrib import admin
from shop.models.commande import CommandeModel


@admin.register(CommandeModel)
class CommandeModelAdmin(admin.ModelAdmin):
    list_display = ('reference', 'date_de_commande', 'user_id', 'total', 'active', 'created_at', 'updated_at')
    search_fields = ('reference', 'user_id__username')
    fields = ('reference', 'user_id', 'active')