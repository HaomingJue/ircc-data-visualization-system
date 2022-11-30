# Generated by Django 4.1 on 2022-11-30 18:02

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ("plan", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="plan",
            name="id",
            field=models.CharField(
                default=uuid.uuid4,
                editable=False,
                max_length=250,
                primary_key=True,
                serialize=False,
            ),
        ),
    ]
