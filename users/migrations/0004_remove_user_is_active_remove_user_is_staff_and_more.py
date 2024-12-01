# Generated by Django 4.2 on 2024-10-23 07:25

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("users", "0003_user_groups_user_is_active_user_is_staff_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="user",
            name="is_active",
        ),
        migrations.RemoveField(
            model_name="user",
            name="is_staff",
        ),
        migrations.AlterField(
            model_name="user",
            name="is_superuser",
            field=models.BooleanField(
                default=False,
                help_text="Designates that this user has all permissions without explicitly assigning them.",
                verbose_name="superuser status",
            ),
        ),
    ]
