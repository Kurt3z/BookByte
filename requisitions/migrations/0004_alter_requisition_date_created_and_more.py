# Generated by Django 5.0.1 on 2024-02-11 01:53

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("requisitions", "0003_requisition_is_delivered_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="requisition",
            name="date_created",
            field=models.DateTimeField(blank=True, editable=False, null=True),
        ),
        migrations.AlterField(
            model_name="requisition",
            name="return_date",
            field=models.DateTimeField(blank=True, editable=False, null=True),
        ),
    ]
