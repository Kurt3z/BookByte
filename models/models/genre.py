import uuid
from django.db import models


class Genre(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created = models.DateTimeField(auto_now=False, auto_now_add=True)
    caption = models.CharField(max_length=200, unique=True)

    def __str__(self):
        return self.caption
