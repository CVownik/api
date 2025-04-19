from django.db import models
import uuid
from users.models import CustomUser
# Create your models here.


class CVInfo(models.Model):
    id= models.UUIDField(primary_key=True,default=uuid.uuid4, editable=False)
    userId = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
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