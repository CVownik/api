from rest_framework import viewsets, filters
from .models import CV, CVInfo
from .serializers import CVSerializer, CVInfoSerializer
from .filters import CVFilter, CVInfoFilter
from rest_framework.parsers import MultiPartParser, FormParser
from django_filters.rest_framework import DjangoFilterBackend
from drf_spectacular.utils import extend_schema, OpenApiParameter
from drf_spectacular.types import OpenApiTypes


class CVViewSet(viewsets.ModelViewSet):
    queryset = CV.objects.all()
    serializer_class = CVSerializer
    parser_classes = (MultiPartParser, FormParser)
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    filterset_class = CVFilter
    ordering_fields = ["thumbnail", "created_at"]

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
                name="ordering",
                type=OpenApiTypes.STR,
                location=OpenApiParameter.QUERY,
                description="Order by: created_at, thumbnail (use - for descending)",
            ),
        ]
    )
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)


class CVInfoViewSet(viewsets.ModelViewSet):
    queryset = CVInfo.objects.all()
    serializer_class = CVInfoSerializer
    parser_classes = (MultiPartParser, FormParser)
    filter_backends = [
        DjangoFilterBackend,
        filters.OrderingFilter,
    ]
    filterset_class = CVInfoFilter
    ordering_fields = ["name", "surname", "created_at"]

    @extend_schema(
        parameters=[
            OpenApiParameter(
                name="id",
                type=OpenApiTypes.UUID,
                location=OpenApiParameter.QUERY,
                description="Filter by ID",
            ),
            OpenApiParameter(
                name="cv_id",
                type=OpenApiTypes.UUID,
                location=OpenApiParameter.QUERY,
                description="Filter by CV ID",
            ),
            OpenApiParameter(
                name="name",
                type=OpenApiTypes.STR,
                location=OpenApiParameter.QUERY,
                description="Filter by name (case insensitive)",
            ),
            OpenApiParameter(
                name="surname",
                type=OpenApiTypes.STR,
                location=OpenApiParameter.QUERY,
                description="Filter by surname (case insensitive)",
            ),
            OpenApiParameter(
                name="about",
                type=OpenApiTypes.STR,
                location=OpenApiParameter.QUERY,
                description="Filter by about field (case insensitive)",
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
                name="ordering",
                type=OpenApiTypes.STR,
                location=OpenApiParameter.QUERY,
                description="Order by: created_at, name, surname (use - for descending)",
            ),
        ]
    )
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)
