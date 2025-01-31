from django.contrib import admin
from boutique.models.vendeur import VendeurModel


@admin.register(VendeurModel)
class VendeurModelAdmin(admin.ModelAdmin):
    list_display = ('nom', 'get_admin_username', 'active', 'created_at', 'updated_at')
    search_fields = ('nom', 'admin_user_id__username')
    fields = ('nom', 'admin_user_id', 'active')

    @admin.display(description='Admin Username')
    def get_admin_username(self, obj):
        return obj.admin_user_id.username