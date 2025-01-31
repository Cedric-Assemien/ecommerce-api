from django.contrib import admin
from customer.models.profil import Profile


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('get_username', 'get_fullname', 'telephone', 'birth_date', 'image')
    search_fields = ('user__username', 'telephone')
    fields = ('user', 'telephone', 'birth_date', 'image')

    @admin.display(description='Username')
    def get_username(self, obj):
        return obj.user.username

    @admin.display(description='Full name')
    def get_fullname(self, obj):
        return obj.user.get_full_name()