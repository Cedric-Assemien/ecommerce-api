from django.db import models


class SousCategorieModel(models.Model):

    class Meta:
        verbose_name = "Sous-Catégorie"
        verbose_name_plural = "Sous-Catégories"

    nom = models.CharField(max_length=254, verbose_name="Nom")
    decsription = models.TextField()

    categorie_id = models.ForeignKey('boutique.CategorieModel', on_delete=models.RESTRICT, related_name="sous_categorie_ids")

    active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Date de création")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Date de dernière modification")


    def __str__(self):
        return self.nom