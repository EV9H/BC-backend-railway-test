# Generated by Django 4.1.5 on 2023-01-09 00:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("base", "0005_alter_word_word"),
    ]

    operations = [
        migrations.AddField(
            model_name="example",
            name="word",
            field=models.ForeignKey(
                null=True, on_delete=django.db.models.deletion.CASCADE, to="base.word"
            ),
        ),
    ]