from rest_framework.routers import DefaultRouter
from customer.viewsets.adresse_de_livraison import AdresseModelViewSet
from customer.viewsets.avis import AvisModelViewSet
from customer.viewsets.moyen_de_paiement import MoyenoDePaiementModelViewSet
from customer.viewsets.profil import ProfileViewSet

router = DefaultRouter()
router.register(r'adresse', AdresseModelViewSet, basename='adresses')
router.register(r'avis', AvisModelViewSet, basename='avis')
router.register(r'moyens_de_paiement', MoyenoDePaiementModelViewSet, basename='moyens_de_paiement')
router.register(r'profile',ProfileViewSet, basename='profile')

urlpatterns = router.urls