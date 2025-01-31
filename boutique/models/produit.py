from django.db import models


class ProduitModel(models.Model):

    class Meta:
        verbose_name = "Produit"
        verbose_name_plural = "Produits"

    nom = models.CharField(max_length=254, verbose_name="Nom")
    decsription = models.TextField()
    prix =  models.FloatField()

    sous_categorie_id = models.ForeignKey('boutique.SousCategorieModel', on_delete=models.RESTRICT, related_name="produits_ids")
    tag_ids = models.ManyToManyField('boutique.TagModel', related_name="tag_article_ids")

    active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Date de création")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Date de dernière modification")

    def __str__(self):
        return self.nom