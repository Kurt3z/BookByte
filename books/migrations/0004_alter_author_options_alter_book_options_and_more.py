# Generated by Django 5.0.1 on 2024-02-06 22:07

import autoslug.fields
from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("books", "0003_alter_author_slug"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="author",
            options={"ordering": ["-created"]},
        ),
        migrations.AlterModelOptions(
            name="book",
            options={"ordering": ["-created"]},
        ),
        migrations.AlterField(
            model_name="author",
            name="slug",
            field=autoslug.fields.AutoSlugField(
                editable=False, null=True, populate_from="get_full_name", unique=True
            ),
        ),
    ]