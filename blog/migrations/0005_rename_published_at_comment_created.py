# Generated by Django 3.2.16 on 2023-01-03 12:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_comment_article'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='published_at',
            new_name='created',
        ),
    ]