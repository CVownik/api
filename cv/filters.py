import django_filters
from .models import CV, CVInfo


class CVFilter(django_filters.FilterSet):
    id = django_filters.UUIDFilter()
    user_id = django_filters.UUIDFilter()
    created_at_from = django_filters.DateTimeFilter(
        field_name="created_at", lookup_expr="gte"
    )
    created_at_to = django_filters.DateTimeFilter(
        field_name="created_at", lookup_expr="lte"
    )

    class Meta:
        model = CV
        fields = ["id", "user_id"]


class CVInfoFilter(django_filters.FilterSet):
    id = django_filters.UUIDFilter()
    cv_id = django_filters.UUIDFilter()
    name = django_filters.CharFilter(field_name="name", lookup_expr="icontains")
    surname = django_filters.CharFilter(field_name="surname", lookup_expr="icontains")
    about = django_filters.CharFilter(field_name="about", lookup_expr="icontains")
    created_at_from = django_filters.DateTimeFilter(
        field_name="created_at", lookup_expr="gte"
    )
    created_at_to = django_filters.DateTimeFilter(
        field_name="created_at", lookup_expr="lte"
    )

    class Meta:
        model = CVInfo
        fields = ["id", "cv_id", "name", "surname", "about"]
