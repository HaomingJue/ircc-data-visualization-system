# Generated by Django 4.1.2 on 2022-10-31 02:25

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0006_alter_userprofile_user_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='user_id',
            field=models.CharField(default=uuid.UUID('49083a94-58c3-11ed-a685-e0d464c9992d'), max_length=250),
        ),
    ]
