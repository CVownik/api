from django.db import models
import uuid
from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin,
)

from django.utils.timezone import now
from datetime import timedelta


def default_premium_expiry():
    return now() + timedelta(days=7)


class Role(models.TextChoices):
    ADMIN = "Admin", "admin"
    USER = "User", "user"
    HR = "Hr", "hr"


class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError("User have to had an email")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        return self.create_user(email, password, **extra_fields)


class CustomUser(AbstractBaseUser, PermissionsMixin):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    role = models.CharField(max_length=20, choices=Role.choices, default=Role.USER)
    created_at = models.DateTimeField(auto_now_add=True)
    premium_expires_at = models.DateTimeField(null=True, blank=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    object = CustomUserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["name"]

    def save(self, *args, **kwargs):
        if self.role == Role.USER:
            self.premium_expires_at = None
        elif self.role == Role.HR and not self.premium_expires_at:
            self.premium_expires_at = default_premium_expiry()

        super().save(*args, **kwargs)

    def __str__(self):
        return self.email


class HR(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.OneToOneField("CustomUser", on_delete=models.CASCADE)
    company_name = models.CharField(max_length=100)
    company_nip = models.CharField(max_length=10)
    telephone = models.CharField(max_length=9)
    country = models.CharField(max_length=100, null=True)
    city = models.CharField(max_length=100)
    street = models.CharField(max_length=100)
    number_street = models.CharField(max_length=5)
    postcode = models.CharField(max_length=10)

    def save(self, *args, **kwargs):
        self.user.role = Role.HR
        self.user.save()
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.user.name} {self.user.surname} - {self.company_name}"
