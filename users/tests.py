import pytest
from users.models import CustomUser, HR, Premium

# Tests for CustomUser model creation and roles


@pytest.mark.django_db
def test_create_user():
    user = CustomUser.objects.create_user(
        email="test@example.com",
        password="test123",
        name="Jan",
        surname="Kowalski",
    )

    assert user.email == "test@example.com"
    assert user.check_password("test123")
    assert user.name == "Jan"
    assert user.surname == "Kowalski"
    assert user.is_active


@pytest.mark.django_db
def test_create_superuser():
    superuser = CustomUser.objects.create_superuser(
        email="admin@example.com",
        password="admin123",
        name="Admin",
        surname="Admin",
    )
    assert superuser.email == "admin@example.com"
    assert superuser.check_password("admin123")
    assert superuser.name == "Admin"
    assert superuser.surname == "Admin"
    assert superuser.is_staff
    assert superuser.is_superuser


@pytest.mark.django_db
def test_create_hr_user():
    user = CustomUser.objects.create_user(
        email="hr@example.com", password="hr123", name="Adam", surname="Nowak"
    )
    hr = HR.objects.create(
        user=user,
        company_name="Plus Tecs",
        company_nip="3421234221",
        telephone="982342123",
        city="Warszawa",
        street="Bałtycka",
        number_street="10",
        postcode="10-232",
    )
    assert user.email == "hr@example.com"
    assert user.check_password("hr123")
    assert user.name == "Adam"
    assert user.surname == "Nowak"
    assert user.is_active
    assert user.hr_role
    assert hr.company_name == "Plus Tecs"
    assert hr.company_nip == "3421234221"
    assert hr.telephone == "982342123"
    assert hr.city == "Warszawa"
    assert hr.street == "Bałtycka"
    assert hr.number_street == "10"
    assert hr.postcode == "10-232"
    assert hr.user == user


@pytest.mark.django_db
def test_create_premium_user():
    user = CustomUser.objects.create_user(
        email="ewaKowal@test.com",
        password="Kowalczyk1@3",
        name="Ewa",
        surname="Kowalczyk",
    )
    premium = Premium.objects.create(user=user)
    assert user.email == "ewaKowal@test.com"
    assert user.check_password("Kowalczyk1@3")
    assert user.name == "Ewa"
    assert user.surname == "Kowalczyk"
    assert user.is_active
    assert user.premium_role
    assert premium.user == user
