import django_filters
from .models import CV, CVInfo


class CVFilter(django_filters.FilterSet):
    user_id = django_filters.UUIDFilter()
    created_at_from = django_filters.DateTimeFilter(field_name="created_at", lookup_expr="gte")
    created_at_to = django_filters.DateTimeFilter(field_name="created_at", lookup_expr="lte")

    class Meta:
        model = CV
        fields = ['user_id']



class CVInfoFilter(django_filters.FilterSet):
    cv_id = django_filters.UUIDFilter()
    name = django_filters.CharFilter()
    surname = django_filters.CharFilter()
    about_contains = django_filters.CharFilter(
        field_name="about", lookup_expr="icontains"
    )
    created_at_from = django_filters.DateTimeFilter(
        field_name="created_at", lookup_expr="gte"
    )
    created_at_to = django_filters.DateTimeFilter(
        field_name="created_at", lookup_expr="lte"
    )

    class Meta:
        model = CVInfo
        fields = ["cv_id", "name", "surname", "about"]
