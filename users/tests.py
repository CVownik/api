import pytest
from users.models import CustomUser, HR, Premium

# Tests for CustomUser model creation and roles


@pytest.mark.django_db
def test_create_user():
    user = CustomUser.object.create_user(
        email="test@example.com",
        password="testpassword123",
        name="Jan",
        surname="Kowalski",
    )

    assert user.email == "test@example.com"
    assert user.check_password("testpassword123")
    assert user.name == "Jan"
    assert user.surname == "Kowalski"
    assert user.is_active


@pytest.mark.django_db
def test_create_superuser():
    superuser = CustomUser.object.create_superuser(
        email="admin@example.com",
        password="adminpassword123",
        name="Admin",
        surname="Admin",
    )
    assert superuser.email == "admin@example.com"
    assert superuser.check_password("adminpassword123")
    assert superuser.name == "Admin"
    assert superuser.surname == "Admin"
    assert superuser.is_staff
    assert superuser.is_superuser


@pytest.mark.django_db
def test_create_hr_user():
    user = CustomUser.object.create_user(
        email="hr@example.com", password="hrpassword123", name="Adam", surname="Nowak"
    )
    hr = HR.objects.create(
        user=user,
        company_name="Tech Solutions",
        company_nip="1234567890",
        telephone="123456789",
        city="Warszawa",
        street="Bałtycka",
        number_street="10",
        postcode="00-001",
    )
    assert user.email == "hr@example.com"
    assert user.check_password("hrpassword123")
    assert user.name == "Adam"
    assert user.surname == "Nowak"
    assert user.is_active
    assert user.hr_role
    assert hr.company_name == "Tech Solutions"
    assert hr.company_nip == "1234567890"
    assert hr.telephone == "123456789"
    assert hr.city == "Warszawa"
    assert hr.street == "Bałtycka"
    assert hr.number_street == "10"
    assert hr.postcode == "00-001"
    assert hr.user == user


@pytest.mark.django_db
def test_create_premium_user():
    user = CustomUser.object.create_user(
        email="ewaKowal@example.com",
        password="userpassword123",
        name="Ewa",
        surname="Kowalczyk",
    )
    premium = Premium.objects.create(user=user)
    assert user.email == "ewaKowal@example.com"
    assert user.check_password("userpassword123")
    assert user.name == "Ewa"
    assert user.surname == "Kowalczyk"
    assert user.is_active
    assert user.premium_role
    assert premium.user == user
