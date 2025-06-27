from django.db import models
import uuid
from users.models import CustomUser

# Create your models here.


def user_avatar_upload_path(instance):
    return f"{instance.user_id.id}/avatars/{instance.id}/avatar.jpg"


def user_thumbnail_upload_path(instance):
    return f"{instance.user_id.id}/thumbnails/{instance.id}/thumbnail.jpg"


class CV(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user_id = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    thumbnail = models.ImageField(
        upload_to=user_thumbnail_upload_path, null=False, blank=True
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"CV for {self.user_id.name} {self.user_id.surname} created at {self.created_at}"


class CVInfo(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    cv_id = models.OneToOneField(CV, on_delete=models.CASCADE, null=False)
    avatar = models.ImageField(upload_to=user_avatar_upload_path, null=True, blank=True)
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    about = models.TextField()

    def __str__(self):
        return f"{self.name}, {self.surname}"


class Contact(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    cv_info_id = models.OneToOneField(CVInfo, on_delete=models.CASCADE)
    telephone = models.CharField(max_length=20)
    email = models.EmailField()
    city = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.cv_info_id.name} {self.cv_info_id.surname} - {self.city}, {self.email}"


class ContactLinks(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    contact_id = models.ForeignKey(Contact, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    link = models.URLField(max_length=200)

    def __str__(self):
        return f"{self.name}: {self.link}"


class Experience(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    cv_id = models.ForeignKey(CV, on_delete=models.CASCADE, null=False)
    position = models.CharField(max_length=255)
    company = models.CharField(max_length=255)
    location = models.CharField(max_length=255, null=True, blank=True)
    start_date = models.DateField(null=True)
    end_date = models.DateField(null=True, blank=True)  # Optional field
    description = models.TextField(max_length=500, null=True, blank=True)

    def __str__(self):
        return (
            f"{self.position} at {self.company} ({self.start_date} - {self.end_date})"
        )


class Duties(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    experience_id = models.ForeignKey(Experience, on_delete=models.CASCADE)
    description = models.TextField(max_length=500)

    def __str__(self):
        return f"Duties for {self.experience_id.position} at {self.experience_id.company}: {self.description}"


class Education(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    cv_id = models.ForeignKey(CV, on_delete=models.CASCADE, null=False, blank=True)
    institution = models.CharField(max_length=255)
    degree = models.CharField(max_length=255)
    start_date = models.DateField(null=True)
    end_date = models.DateField(null=True, blank=True)  # Optional field
    description = models.TextField(
        max_length=500, null=True, blank=True
    )  # Optional field

    def __str__(self):
        return f"{self.degree} from {self.institution} ({self.start_date} - {self.end_date})"


class Languages(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    cv_id = models.ForeignKey(CV, on_delete=models.CASCADE, null=False, blank=True)
    language = models.CharField(max_length=100)
    language_lever = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.language} - {self.language_lever}"


class Interests(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    cv_id = models.ForeignKey(CV, on_delete=models.CASCADE, null=False, blank=True)
    interest = models.CharField(max_length=255)

    def __str__(self):
        return (
            f"Interest: {self.interest} for "
            f"{self.cv_info_id.name} {self.cv_info_id.surname}"
        )


class SoftSkills(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    cv_id = models.ForeignKey(CV, on_delete=models.CASCADE, null=False, blank=True)
    skill = models.CharField(max_length=255)

    def __str__(self):
        return (
            f"Soft Skill: {self.skill} for "
            f"{self.cv_info_id.name} {self.cv_info_id.surname}"
        )


class HardSkills(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    cv_id = models.ForeignKey(CV, on_delete=models.CASCADE, null=False, blank=True)
    skill = models.CharField(max_length=255)

    def __str__(self):
        return (
            f"Hard Skill: {self.skill} for "
            f"{self.cv_info_id.name} {self.cv_info_id.surname}"
        )


class Projects(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    cv_id = models.ForeignKey(CV, on_delete=models.CASCADE, null=False, blank=True)
    name = models.CharField(max_length=255)
    description = models.TextField(max_length=500, null=True, blank=True)
    link = models.URLField(max_length=200, null=True, blank=True)
    start_date = models.DateField(null=True)
    end_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"Project: {self.name} ({self.start_date} - {self.end_date})"
