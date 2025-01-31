from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()
MP_CHOICES = {
    "mobile": "Mobile Money",
    "visa": "Visa",
    "wave": "Wave",
    "paypal": "Paypal",
}


class MoyenoDePaiementModel(models.Model):

    class Meta:
        verbose_name = "Moyen de Paiment"
        verbose_name_plural = "Moyens de Paiment"

    type = models.CharField(max_length=254, verbose_name="Type", choices=MP_CHOICES, default="mobile")
    carte = models.CharField(max_length=254, verbose_name="Numéro de la carte", null=True, blank=True)
    cvc = models.CharField(max_length=254, verbose_name="CVC", null=True, blank=True)
    mois_expiration = models.CharField(max_length=20, verbose_name="Mois expiration", null=True, blank=True)
    annee_expiration = models.CharField(max_length=20, verbose_name="Année expiration", null=True, blank=True)
    adresse_paypal = models.CharField(max_length=20, verbose_name="Adresse Paypal", null=True, blank=True)
    numero = models.CharField(max_length=20, verbose_name="numéro", null=True, blank=True)

    user_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_mp_ids")

    active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Date de création")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Date de dernière modification")

    def __str__(self):
        
        return self.type
        