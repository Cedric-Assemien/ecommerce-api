from rest_framework.routers import DefaultRouter
from boutique.viewsets.categorie import CategorieModelViewSet
from boutique.viewsets.produit import ProduitModelViewSet
from boutique.viewsets.sous_categorie import SousCategorieModelViewSet
from boutique.viewsets.vendeur import VendeurModelViewSet

router = DefaultRouter()
router.register(r'categories', CategorieModelViewSet, basename='categories')
router.register(r'produits', ProduitModelViewSet, basename='produits')
router.register(r'sous_categories', SousCategorieModelViewSet, basename='sous_categories')
router.register(r'vendeurs', VendeurModelViewSet, basename='vendeurs')

urlpatterns = router.urls