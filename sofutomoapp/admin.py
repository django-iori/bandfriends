from django.contrib import admin
from django.db.models.fields.files import ImageField
from .models import *

# Register your models here.

admin.site.register(GuestModel)
admin.site.register(HostModel)
admin.site.register(GoodModel)
admin.site.register(MatchModel)
admin.site.register(Room)
admin.site.register(Message)


