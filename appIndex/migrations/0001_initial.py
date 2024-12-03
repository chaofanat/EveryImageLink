# Generated by Django 5.1.1 on 2024-09-27 12:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="application",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("name", models.CharField(max_length=50)),
                ("description", models.TextField()),
                ("url", models.URLField()),
                (
                    "icon",
                    models.ImageField(
                        default="appIndex/app_icon/default.png",
                        upload_to="appIndex/app_icon",
                    ),
                ),
                ("is_active", models.BooleanField(default=True)),
                ("create_time", models.DateTimeField(auto_now_add=True)),
                ("update_time", models.DateTimeField(auto_now=True)),
            ],
            options={
                "verbose_name": "application",
                "verbose_name_plural": "applications",
                "ordering": ("-create_time",),
            },
        ),
    ]