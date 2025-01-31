from django.contrib import admin
from boutique.models.tag import TagModel



@admin.register(TagModel)
class TagModelAdmin(admin.ModelAdmin):
    list_display = ('nom', 'active', 'created_at', 'updated_at')
    search_fields = ('nom',)
    fields = ('nom', 'active')