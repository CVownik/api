from rest_framework.routers import DefaultRouter
from .views import CVViewSet, CVInfoViewSet, ContactView
from django.urls import path, include


router = DefaultRouter()
router.register(r"CV", CVViewSet, basename="CV")
router.register(r"CVInfo", CVInfoViewSet, basename="CVInfo")
router.register(r"Contact", ContactView, basename="Contact")

urlpatterns = [
    path("", include(router.urls)),
]
