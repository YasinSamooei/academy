# Generated by Django 4.2 on 2023-12-29 16:19

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("catalogue", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="producttype",
            name="description",
            field=models.TextField(blank=True, null=True),
        ),
    ]