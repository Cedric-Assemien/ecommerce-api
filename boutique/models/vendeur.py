from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class VendeurModel(models.Model):

    class Meta:
        verbose_name = "Tag"
        verbose_name_plural = "Tags"

    nom = models.CharField(max_length=254, verbose_name="Nom")

    admin_user_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name="vendeur_ids")
    
    active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Date de création")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Date de dernière modification")


    def __str__(self):
        return self.nom