import uuid
from django.db import models


class Country(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created = models.DateTimeField(auto_now=False, auto_now_add=True)
    name = models.CharField(max_length=100, unique=True)
    code = models.CharField(max_length=5, unique=True)

    class Meta:
        verbose_name_plural = "Countries"

    def __str__(self):
        return self.code
