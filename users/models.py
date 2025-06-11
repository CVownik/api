from django.db import models
import uuid
from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin,
)

from django.utils.timezone import now
from datetime import timedelta


def default_hr_expiry_start():
    return now() + timedelta(days=7)


def default_hr_expiry():
    return now() + timedelta(days=30)


def default_premium_expiry():
    return now() + timedelta(days=30)


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
    hr_role = models.BooleanField(default=False)
    premium_role = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    trial_used_hr = models.BooleanField(default=False)
    hr_expires_at = models.DateTimeField(null=True, blank=True)
    premium_expires_at = models.DateTimeField(null=True, blank=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = CustomUserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["name"]

    def save(self, *args, **kwargs):
        if not self.hr_role:
            self.hr_expires_at = None
        if not self.premium_role:
            self.premium_expires_at = None
        if self.hr_role:
            if not self.hr_expires_at:
                if not self.trial_used_hr:
                    self.hr_expires_at = default_hr_expiry_start()
                    self.trial_used_hr = True
                else:
                    self.hr_expires_at = default_hr_expiry()
        if self.premium_role:
            if not self.premium_expires_at:
                self.premium_expires_at = default_premium_expiry()

        super().save(*args, **kwargs)

    def __str__(self):
        return self.email

    def get_id(self):
        return self.id


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
        self.user.hr_role = True

        self.user.save()
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.user.name} {self.user.surname} - {self.company_name}"


class Premium(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.OneToOneField("CustomUser", on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        self.user.premium_role = True

        self.user.save()
        super().save(*args, **kwargs)

    def __str__(self):
        return (
            f"{self.user.name} {self.user.surname} - "
            f"Premium until {self.user.premium_expires_at}"
        )
