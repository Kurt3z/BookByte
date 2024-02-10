import uuid
from autoslug import AutoSlugField
from django.db import models

from .publisher import Publisher
from .genre import Genre
from .country import Country


class Content(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created = models.DateTimeField(auto_now=False, auto_now_add=True)
    title = models.CharField(max_length=250)
    publication_date = models.DateField(auto_now=False, auto_now_add=False)
    quantity = models.PositiveIntegerField(default=1)
    summary = models.TextField()
    cover = models.ImageField(upload_to="covers/")
    slug = AutoSlugField(populate_from="title", unique=True,
                         db_index=True, editable=False)
    publisher = models.ForeignKey(
        Publisher, on_delete=models.SET_NULL, null=True)
    genre = models.ManyToManyField(Genre)
    language = models.ForeignKey(Country, on_delete=models.PROTECT)

    class Meta:
        verbose_name_plural = "Content"

    def __str__(self):
        return f"{self.title}"
