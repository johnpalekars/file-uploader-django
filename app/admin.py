from django.contrib import admin
from app.models import Files
from app.models import CustomUser


# Register your models here.

admin.site.register(Files)
admin.site.register(CustomUser)
