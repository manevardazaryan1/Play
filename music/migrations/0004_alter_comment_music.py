# Generated by Django 4.1.2 on 2023-02-24 18:20

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("music", "0003_comment"),
    ]

    operations = [
        migrations.AlterField(
            model_name="comment",
            name="music",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="music_comments",
                to="music.music",
            ),
        ),
    ]
