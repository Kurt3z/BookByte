# Generated by Django 5.0.1 on 2024-02-07 01:16

import django.core.validators
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("accounts", "0004_alter_contact_profile_image"),
        ("models", "0005_city"),
    ]

    operations = [
        migrations.AlterField(
            model_name="contact",
            name="building",
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="contact",
            name="district",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="models.district",
            ),
        ),
        migrations.AlterField(
            model_name="contact",
            name="gender",
            field=models.CharField(
                blank=True,
                choices=[("M", "Masculino"), ("F", "Feminino"), ("O", "Outro")],
                max_length=1,
                null=True,
            ),
        ),
        migrations.AlterField(
            model_name="contact",
            name="postal_code",
            field=models.CharField(
                blank=True,
                max_length=8,
                null=True,
                validators=[
                    django.core.validators.RegexValidator(
                        message="Insira um Código-Postal válido.",
                        regex="^\\d{4}-\\d{3}$",
                    )
                ],
            ),
        ),
        migrations.AlterField(
            model_name="contact",
            name="street",
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
    ]
