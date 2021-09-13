from django.contrib import admin
from django.db.models.fields.files import ImageField
from .models import GuestModel, HostModel, ImageModel

# Register your models here.

admin.site.register(GuestModel)
admin.site.register(HostModel)
admin.site.register(ImageModel)

