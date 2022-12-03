# Generated by Django 3.2.16 on 2022-12-01 02:25

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('files', '0005_alter_userfile_uuid_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='userfile',
            name='size',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='userfile',
            name='uuid_name',
            field=models.UUIDField(default=uuid.UUID('57c06417-b349-42e4-90e2-5839d8e35537')),
        ),
    ]