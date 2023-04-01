from django.db import models


class UpdateAndCreateDateMixin(models.Model):
    """
    Add `created_at` and `updated_at` fields. These fields will update automatically.
    """

    class Meta:
        abstract = True

    created_at = models.DateTimeField(verbose_name="Дата создания", auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name="Дата обновления", auto_now=True)