from rest_framework.routers import DefaultRouter
from .views import (
    UserRegisterView,
    HRRegisterView,
    PremiumRegisterView,
    UserView,
    HRView,
    PremiumView,
)
from django.urls import path, include


router = DefaultRouter()
router.register(r"User", UserView, basename="User")
router.register(r"HR", HRView, basename="HR")
router.register(r"Premium", PremiumView, basename="Premium")


urlpatterns = [
    path("register/", UserRegisterView.as_view(), name="user-register"),
    path("register/hr/", HRRegisterView.as_view(), name="hr-register"),
    path("register/premium/", PremiumRegisterView.as_view(), name="premium-register"),
    path("", include(router.urls)),
]
