from django.contrib.auth.models import AbstractUser
from django.core.validators import MinLengthValidator
from django.db import models

from users.validators import validate_firstname


class CustomUser(AbstractUser):
    pass


# class User(models.Model):
#     username = models.CharField(max_length=200)
#     password = models.CharField(max_length=200)
#     email = models.EmailField()
#     last_login = models.DateTimeField(blank=True, null=True, verbose_name='last login')
#
#     def __str__(self):
#         return self.username


class UserDetail(models.Model):
    username = models.CharField(max_length=200)
    firstname = models.CharField(max_length=200)
    lastname = models.CharField(max_length=200, validators=[validate_firstname])
    phone = models.CharField(max_length=200, validators=[MinLengthValidator(10)])
    email = models.EmailField(max_length=200)

    def __str__(self):
        return self.username
