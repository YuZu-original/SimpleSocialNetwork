import datetime

from django.contrib.auth.models import AbstractUser
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

from utils.model_mixins import UpdateAndCreateDateMixin
from utils.model_validators import EmailDomainValidator


class User(AbstractUser, UpdateAndCreateDateMixin):
    email = models.EmailField(
        verbose_name="Почта",
        blank=True,
        validators=[EmailDomainValidator(available_domains=["mail.ru", "yandex.ru"])],
    )
    phone_number = PhoneNumberField(
        verbose_name="Номер телефона", null=False, blank=False, unique=True
    )
    date_of_birth = models.DateField(
        verbose_name="Дата рождения", default=datetime.date.today
    )
