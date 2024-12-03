# Generated by Django 5.1.1 on 2024-09-05 13:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("appUser", "0005_alter_profile_image"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="profile",
            options={
                "default_related_name": "profile",
                "get_latest_by": "created_at",
                "ordering": ["-created_at"],
            },
        ),
    ]