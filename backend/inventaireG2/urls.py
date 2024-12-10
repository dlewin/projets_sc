from django.urls import include, path
from rest_framework import routers
from .views import YuzeViewSet

router = routers.DefaultRouter()
router.register(r'yuzes', YuzeViewSet)

urlpatterns = [
    path('', include(router.urls)),
]