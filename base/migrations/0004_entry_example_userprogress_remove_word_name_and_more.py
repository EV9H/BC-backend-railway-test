# Generated by Django 4.1.5 on 2023-01-08 21:34

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.db.models.fields


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("base", "0003_remove_meaning_attribute_id_meaning_attribute_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="Entry",
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
                ("meaning", models.CharField(max_length=100)),
                ("attribute", models.CharField(max_length=40)),
                ("progress", models.FloatField(default=0.0)),
            ],
        ),
        migrations.CreateModel(
            name="Example",
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
                ("example", models.TextField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name="UserProgress",
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
                (
                    "user",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                ("user_base", models.ManyToManyField(to="base.entry")),
            ],
        ),
        migrations.RemoveField(model_name="word", name="name",),
        migrations.AddField(
            model_name="word",
            name="word",
            field=models.CharField(max_length=40, null=True),
        ),
        migrations.DeleteModel(name="Meaning",),
        migrations.AddField(
            model_name="entry",
            name="example",
            field=models.ManyToManyField(to="base.example"),
        ),
        migrations.AddField(
            model_name="entry",
            name="word",
            field=models.ForeignKey(
                on_delete=django.db.models.fields.CharField, to="base.word"
            ),
        ),
    ]
