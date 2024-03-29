import uuid
from autoslug import AutoSlugField
from django.db import models

from models.models import Country


class Author(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created = models.DateTimeField(auto_now=False, auto_now_add=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    birthdate = models.DateField(
        auto_now=False, auto_now_add=False, null=True, blank=True)
    country = models.ForeignKey(
        Country, on_delete=models.SET_NULL, null=True, blank=True)
    biography = models.TextField(null=True, blank=True)
    personal_website = models.URLField(blank=True, null=True)
    picture = models.ImageField(upload_to="authors/", null=True, blank=True)
    slug = AutoSlugField(populate_from="get_full_name", unique=True,
                         db_index=True, editable=False, null=True)

    class Meta:
        ordering = ["-created"]

    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"

    def __str__(self):
        return self.get_full_name()
