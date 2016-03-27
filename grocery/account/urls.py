from django.conf.urls import include, patterns, url
from account import views

from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'account', views.AccountViewSet)
router.register(r'authentication', views.AuthenticationViewSet)
router.register(r'item', views.ItemViewSet)
router.register(r'watching history', views.WatchingHistoryViewSet)
router.register(r'shopping history', views.ShoppingHistoryViewSet)
router.register(r'shopping bag', views.ShoppingBagViewSet)

urlpatterns = [
    # REST api
    url(r'^api/', include(router.urls)),
]