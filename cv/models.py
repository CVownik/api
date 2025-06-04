from django.db import models
import uuid
from users.models import CustomUser

# Create your models here.


class CVInfo(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    userId = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to=f"{CustomUser.get_id}/", null=True)
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    telephone = models.CharField(max_length=9)
    city = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    about = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name}, {self.surname}, {self.country}"


class Contact(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    cv_info_id = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    telephone = models.CharField(max_length=20)
    email = models.EmailField()
    city = models.CharField(max_length=255)


class ContactLinks(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    contact_id = models.ForeignKey(Contact, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    link = models.CharField(max_length=255)


class Experience(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    cv_info_id = models.ForeignKey(CVInfo, on_delete=models.CASCADE)
    position = models.CharField(max_length=255)
    company = models.CharField(max_length=255)
    start_date = models.DateField(null=True)
    end_date = models.DateField(null=True)


class Duties(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    experience_id = models.ForeignKey(Experience, on_delete=models.CASCADE)
    description = models.TextField(max_length=500)
