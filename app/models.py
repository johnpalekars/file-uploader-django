from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import AbstractUser
from django.utils.translation import ugettext_lazy as _
from app.managers import CustomUserManager
# Create your models here.


class CustomUser(AbstractUser):

    first_name = models.CharField(_('first name'), max_length=30, blank=True)
    last_name = models.CharField(_('last name'), max_length=150, blank=True)
    username = models.CharField(
        _('username'),
        max_length=150,
        unique=True,
        error_messages={
            'unique': _("A user with that username already exists."),
        },
    )
    email = models.EmailField(_('email address'), unique=True)

    EMAIL_FIELD = 'email'
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'email']

    objects = CustomUserManager()

    def __str__(self):

        return self.email


class Files(models.Model):
    username = models.CharField(max_length=256)
    fileName = models.CharField(max_length=256)
    fileLocation = models.FileField(
        max_length=256, upload_to='files/', null=True, verbose_name="")
    modified = models.DateField(auto_now=True)

    def __str__(self):
        return self.fileName

    class meta:
        db_table = "app_user"


class Friend(models.Model):
    name = models.CharField(max_length=256)

    def __str__(self):
        return self.name


class Abhi(models.Model):
    username = models.CharField(max_length=256)
    friend = models.ForeignKey('Friend', on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.username





    
