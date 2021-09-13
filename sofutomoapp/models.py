from django.db import models
from django.contrib.auth.models import User
from django_mysql.models import ListCharField
import uuid
from django.utils import timezone
# Create your models here.

class GuestModel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=20, blank=True)
    gender = models.CharField(max_length=20, blank=True)
    #image = models.ImageField(upload_to='image/')
    age = models.IntegerField(null=True, blank=True, default=0)
    email = models.EmailField(max_length=240)

class HostModel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=20, blank=True)
    gender = models.CharField(max_length=20, blank=True)
    #image = models.ImageField(upload_to='')
    age = models.IntegerField(null=True, blank=True, default=0)
    email = models.EmailField(max_length=240)
    good_counts = models.IntegerField(null=True, blank=True, default=0)
    #event情報
    location = models.CharField(max_length=30, blank=True) 
    member = models.IntegerField(null=True, blank=True, default=0)
    event_date = models.DateField(null=True, blank=True)
    event_time = models.TimeField(null=True, blank=True)

class ImageModel(models.Model):
    image=models.ImageField(upload_to='')

class GoodModel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    good_user = models.CharField(max_length=20, blank=True)
    gender = models.CharField(max_length=20, blank=True)
    #image = models.ImageField(upload_to='')
    age = models.IntegerField(null=True, blank=True, default=0)
    email = models.EmailField(max_length=240)

class Room(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    name = models.CharField(max_length=50)
    created_at = models.DateTimeField(default=timezone.now)

class Message(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    room = models.ForeignKey(
        Room,
        blank=True,
        null=True,
        related_name='room_meesages',
        on_delete=models.CASCADE
    )
    name = models.CharField(max_length=50)
    content = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)

