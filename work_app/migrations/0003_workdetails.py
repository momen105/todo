# Generated by Django 5.0 on 2023-12-28 16:12

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("work_app", "0002_todowork_note"),
    ]

    operations = [
        migrations.CreateModel(
            name="WorkDetails",
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
                ("details", models.TextField()),
                (
                    "todo_work",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="todo_work",
                        to="work_app.todowork",
                    ),
                ),
            ],
        ),
    ]