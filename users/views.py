from rest_framework import generics
from rest_framework import viewsets, filters
from rest_framework.permissions import AllowAny
from users.models import CustomUser, HR, Premium
from users.serializers import (
    UserRegisterSerializer,
    HRRegisterSerializer,
    PremiumRegisterSerializer,
    UserSerializer,
    HRSerializer,
    PremiumSerializer,
)
from django_filters.rest_framework import DjangoFilterBackend
from drf_spectacular.utils import extend_schema, OpenApiParameter
from drf_spectacular.types import OpenApiTypes
from .filters import UserFilter, HRFilter, PremiumFilter


class UserRegisterView(generics.CreateAPIView):
    queryset = CustomUser.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = UserRegisterSerializer


class HRRegisterView(generics.CreateAPIView):
    queryset = HR.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = HRRegisterSerializer


class PremiumRegisterView(generics.CreateAPIView):
    queryset = HR.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = PremiumRegisterSerializer


class UserView(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
    filter_backends = [
        DjangoFilterBackend,
        filters.OrderingFilter,
    ]
    filterset_class = UserFilter
    ordering_fields = ["email","name","surname","created_at", "hr_expires_at","premium_expires_at"]


    @extend_schema(
        parameters=[
            OpenApiParameter(
                name="id",
                type=OpenApiTypes.UUID,
                location=OpenApiParameter.QUERY,
                description="Filter by ID",
            ),
            OpenApiParameter(
                name="email",
                type=OpenApiTypes.EMAIL,
                location=OpenApiParameter.QUERY,
                description="Filter by email",
            ),
            OpenApiParameter(
                name="name",
                type=OpenApiTypes.STR,
                location=OpenApiParameter.QUERY,
                description="Filter by name",
            ),
            OpenApiParameter(
                name="surname",
                type=OpenApiTypes.STR,
                location=OpenApiParameter.QUERY,
                description="Filter by surname",
            ),
            OpenApiParameter(
                name="hr_role",
                type=OpenApiTypes.BOOL,
                location=OpenApiParameter.QUERY,
                description="Filter by hr_role",
            ),
            OpenApiParameter(
                name="premium_role",
                type=OpenApiTypes.BOOL,
                location=OpenApiParameter.QUERY,
                description="Filter by premium_role",
            ),
            OpenApiParameter(
                name="created_at_from",
                type=OpenApiTypes.DATETIME,
                location=OpenApiParameter.QUERY,
                description="Filter by creation date from",
            ),
            OpenApiParameter(
                name="created_at_to",
                type=OpenApiTypes.DATETIME,
                location=OpenApiParameter.QUERY,
                description="Filter by creation date to",
            ),
            OpenApiParameter(
                name="trial_used_hr",
                type=OpenApiTypes.BOOL,
                location=OpenApiParameter.QUERY,
                description="Filter by trial used HR",
            ),
            OpenApiParameter(
                name="hr_expires_at_from",
                type=OpenApiTypes.DATETIME,
                location=OpenApiParameter.QUERY,
                description="Filter by hr expires date from",
            ),
            OpenApiParameter(
                name="hr_expires_at_to",
                type=OpenApiTypes.DATETIME,
                location=OpenApiParameter.QUERY,
                description="Filter by hr expires date to",
            ),
            OpenApiParameter(
                name="premium_expires_at_from",
                type=OpenApiTypes.DATETIME,
                location=OpenApiParameter.QUERY,
                description="Filter by premium expires date from",
            ),
            OpenApiParameter(
                name="premium_expires_at_to",
                type=OpenApiTypes.DATETIME,
                location=OpenApiParameter.QUERY,
                description="Filter by premium expires date to",
            ),
            OpenApiParameter(
                name="is_active",
                type=OpenApiTypes.BOOL,
                location=OpenApiParameter.QUERY,
                description="Filter by active",
            ),
            OpenApiParameter(
                name="is_staff",
                type=OpenApiTypes.BOOL,
                location=OpenApiParameter.QUERY,
                description="Filter by staff",
            ),

        ]
    )
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)


class HRView(viewsets.ModelViewSet):
    queryset = HR.objects.all()
    serializer_class = HRSerializer
    filter_backends = [
        DjangoFilterBackend,
        filters.OrderingFilter,
    ]
    filterset_class = HRFilter

    @extend_schema(
        parameters=[
            OpenApiParameter(
                name="id",
                type=OpenApiTypes.UUID,
                location=OpenApiParameter.QUERY,
                description="Filter by ID",
            ),
             OpenApiParameter(
                name="user_id",
                type=OpenApiTypes.UUID,
                location=OpenApiParameter.QUERY,
                description="Filter by user ID",
            ),
            OpenApiParameter(
                name="company_name",
                type=OpenApiTypes.STR,
                location=OpenApiParameter.QUERY,
                description="Filter by company name",
            ),
            OpenApiParameter(
                name="company_nip",
                type=OpenApiTypes.STR,
                location=OpenApiParameter.QUERY,
                description="Filter by company nip",
            ),
            OpenApiParameter(
                name="telephone",
                type=OpenApiTypes.STR,
                location=OpenApiParameter.QUERY,
                description="Filter by telephone",
            ),
            OpenApiParameter(
                name="country",
                type=OpenApiTypes.STR,
                location=OpenApiParameter.QUERY,
                description="Filter by country",
            ),
            OpenApiParameter(
                name="city",
                type=OpenApiTypes.STR,
                location=OpenApiParameter.QUERY,
                description="Filter by city",
            ),
            OpenApiParameter(
                name="street",
                type=OpenApiTypes.STR,
                location=OpenApiParameter.QUERY,
                description="Filter by street",
            ),
            OpenApiParameter(
                name="number_street",
                type=OpenApiTypes.STR,
                location=OpenApiParameter.QUERY,
                description="Filter by street number",
            ),
            OpenApiParameter(
                name="postcode",
                type=OpenApiTypes.STR,
                location=OpenApiParameter.QUERY,
                description="Filter by postcode",
            ),
            ])
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)


class PremiumView(viewsets.ModelViewSet):
    queryset = Premium.objects.all()
    serializer_class = PremiumSerializer
    filter_backends = [
        DjangoFilterBackend,
    ]
    filterset_class = PremiumFilter

    @extend_schema(
        parameters=[
            OpenApiParameter(
                name="id",
                type=OpenApiTypes.UUID,
                location=OpenApiParameter.QUERY,
                description="Filter by ID",
            ),
             OpenApiParameter(
                name="user_id",
                type=OpenApiTypes.UUID,
                location=OpenApiParameter.QUERY,
                description="Filter by user ID",
            ),
            ])
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)
