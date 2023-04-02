from typing import Iterable, Optional

from django.core.exceptions import ValidationError
from django.utils.deconstruct import deconstructible


@deconstructible
class EmailDomainValidator:
    message = "Enter a valid email domain."

    def __init__(
        self,
        available_domains: Optional[Iterable[str]] = None,
        unavailable_domains: Optional[Iterable[str]] = None,
    ):
        self.available_domains = available_domains
        self.unavailable_domains = unavailable_domains

    def __call__(self, value):
        user_part, domain_part = value.rsplit("@", 1)

        if self.available_domains and domain_part not in self.available_domains:
            raise ValidationError(self.message)

        if self.unavailable_domains and domain_part in self.unavailable_domains:
            raise ValidationError(self.message)

        return value
