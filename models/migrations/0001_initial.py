# Generated by Django 5.0.1 on 2024-01-29 20:57

import autoslug.fields
import django.db.models.deletion
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Country",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("created", models.DateTimeField(auto_now_add=True)),
                ("name", models.CharField(max_length=100, unique=True)),
                ("code", models.CharField(max_length=5, unique=True)),
            ],
            options={
                "verbose_name_plural": "Countries",
            },
        ),
        migrations.CreateModel(
            name="Genre",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("created", models.DateTimeField(auto_now_add=True)),
                ("caption", models.CharField(max_length=200, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name="Publisher",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("created", models.DateTimeField(auto_now_add=True)),
                ("name", models.CharField(max_length=100)),
                ("email", models.EmailField(blank=True, max_length=254, null=True)),
                ("website", models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name="Content",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("created", models.DateTimeField(auto_now_add=True)),
                ("title", models.CharField(max_length=250)),
                ("publication_date", models.DateField()),
                ("quantity", models.PositiveIntegerField(default=1)),
                ("summary", models.TextField()),
                ("cover", models.ImageField(upload_to="covers/")),
                (
                    "slug",
                    autoslug.fields.AutoSlugField(
                        editable=False, populate_from="title", unique=True
                    ),
                ),
                (
                    "language",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT, to="models.country"
                    ),
                ),
                ("genre", models.ManyToManyField(to="models.genre")),
                (
                    "publisher",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="models.publisher",
                    ),
                ),
            ],
            options={
                "verbose_name_plural": "Content",
            },
        ),
    ]
