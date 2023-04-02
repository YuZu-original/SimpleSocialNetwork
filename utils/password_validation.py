from django.core.exceptions import ValidationError
from django.utils.translation import ngettext


class HasDigitsValidator:
    """
    Validate that the password has digits.
    """

    def __init__(self, min_count: int = 1):
        self.min_count = min_count

    def validate(self, password, user=None):
        digits_count = sum(c.isdigit() for c in password)
        if digits_count < self.min_count:
            raise ValidationError(
                ngettext(
                    "This password must contain at least " "%(min_count)d digit.",
                    "This password must contain at least " "%(min_count)d digits.",
                    self.min_count,
                ),
                params={"min_count": self.min_count},
            )

    def get_help_text(self):
        return ngettext(
            "Your password must contain at least %(min_count)d digit.",
            "Your password must contain at least %(min_count)d digits.",
            self.min_count,
        ) % {"min_count": self.min_count}
