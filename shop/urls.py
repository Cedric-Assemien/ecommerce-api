from rest_framework.routers import DefaultRouter
from shop.viewsets.commande import CommandeModelViewSet
from shop.viewsets.panier import PanierModelViewSet
from shop.viewsets.produit_commande import ProduitCommandeModelViewSet
from shop.viewsets.produit_panier import ProduitPanierModelViewSet

router = DefaultRouter()
router.register(r'commandes', CommandeModelViewSet, basename='commandes')
router.register(r'panier', PanierModelViewSet, basename='panier')
router.register(r'produit_commande', ProduitCommandeModelViewSet, basename='produit_commande')
router.register(r'produits_panier', ProduitPanierModelViewSet, basename='produits_panier')

urlpatterns = router.urls