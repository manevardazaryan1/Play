# Generated by Django 4.1.2 on 2023-02-14 22:14

from django.db import migrations, models
import signer.models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Signer",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("first_name", models.CharField(max_length=155)),
                ("last_name", models.CharField(max_length=155)),
                ("description", models.TextField(blank=True, null=True)),
                ("date_of_birth", models.DateField()),
                (
                    "image",
                    models.ImageField(blank=True, upload_to=signer.models.upload_image),
                ),
            ],
            options={
                "verbose_name": "Signer",
                "verbose_name_plural": "Signers",
            },
        ),
    ]