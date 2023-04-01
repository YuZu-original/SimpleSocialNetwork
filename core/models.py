from django.contrib.auth.models import AbstractUser
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

from utils.model_mixins import UpdateAndCreateDateMixin


class User(AbstractUser, UpdateAndCreateDateMixin):
    phone_number = PhoneNumberField(verbose_name="Номер телефона", null=False, blank=False, unique=True)
    date_of_birth = models.DateField(verbose_name="Дата рождения")