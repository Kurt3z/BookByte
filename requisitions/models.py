import uuid
from django.db import models
from django.utils import timezone
from datetime import timedelta

from accounts.models import Reader, Librarian
from models.models import Content


class Requisition(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    reader = models.ForeignKey(
        Reader, on_delete=models.PROTECT, null=True, blank=True)
    librarian = models.ForeignKey(
        Librarian, on_delete=models.PROTECT, null=True, blank=True)
    contents = models.ManyToManyField(Content)
    is_complete = models.BooleanField(default=False, null=True, blank=False)
    is_delivered = models.BooleanField(default=False, null=True, blank=False)
    date_created = models.DateTimeField(
        auto_now=False, auto_now_add=False, editable=False, null=True, blank=True)
    return_date = models.DateTimeField(
        auto_now=False, auto_now_add=False, editable=False, null=True, blank=True)

    class Meta:
        ordering = ["-date_created"]

    def __str__(self):
        return str(self.id)

    def submit_requisition(self):
        if not self.is_complete:
            self.is_complete = True
            self.date_created = timezone.now()
            self.return_date = self.date_created + timedelta(days=30)
            self.save()
