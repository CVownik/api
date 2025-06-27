import django_filters
from .models import CustomUser, HR, Premium


class UserFilter(django_filters.FilterSet):
    id = django_filters.UUIDFilter()
    email = django_filters.CharFilter(field_name="email", lookup_expr="icontains")
    name = django_filters.CharFilter(field_name="name", lookup_expr="icontains")
    surname = django_filters.CharFilter(field_name="surname", lookup_expr="icontains")
    created_at_from = django_filters.DateTimeFilter(
        field_name="created_at", lookup_expr="gte"
    )
    created_at_to = django_filters.DateTimeFilter(
        field_name="created_at", lookup_expr="lte"
    )
    hr_role = django_filters.BooleanFilter()
    premium_role = django_filters.BooleanFilter()
    trial_used_hr = django_filters.BooleanFilter()
    hr_expires_at_from = django_filters.DateTimeFilter(
        field_name="hr_expires_at", lookup_expr="gte"
    )
    hr_expires_at_to = django_filters.DateTimeFilter(
        field_name="hr_expires_at", lookup_expr="lte"
    )
    premium_expires_at_from = django_filters.DateTimeFilter(
        field_name="premium_expires_at", lookup_expr="gte"
    )
    premium_expires_at_to = django_filters.DateTimeFilter(
        field_name="premium_expires_at", lookup_expr="lte"
    )
    is_active = django_filters.BooleanFilter()
    is_staff = django_filters.BooleanFilter()

    class Meta:
        model = CustomUser
        fields = [
            "id",
            "email",
            "name",
            "surname",
            "hr_role",
            "premium_role",
            "is_active",
            "is_staff",
        ]


class HRFilter(django_filters.FilterSet):
    id = django_filters.UUIDFilter()
    user_id = django_filters.UUIDFilter()
    company_name = django_filters.CharFilter(
        field_name="company_name", lookup_expr="icontains"
    )
    company_nip = django_filters.CharFilter(
        field_name="company_nip", lookup_expr="icontains"
    )
    telephone = django_filters.CharFilter(
        field_name="telephone", lookup_expr="icontains"
    )
    country = django_filters.CharFilter(field_name="country", lookup_expr="icontains")
    city = django_filters.CharFilter(field_name="city", lookup_expr="icontains")
    street = django_filters.CharFilter(field_name="street", lookup_expr="icontains")
    number_street = django_filters.CharFilter(
        field_name="number_street", lookup_expr="icontains"
    )
    postcode = django_filters.CharFilter(field_name="postcode", lookup_expr="icontains")

    class Meta:
        model = HR
        fields = ["id", "user_id", "company_name", "company_nip","telephone","country","city","street","number_street", "postcode"]


class PremiumFilter(django_filters.FilterSet):
    id = django_filters.UUIDFilter()
    user_id = django_filters.UUIDFilter()

    class Meta:
        model = Premium
        fields = ["id", "user_id"]
