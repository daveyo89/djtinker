# Generated by Django 3.1.2 on 2020-10-25 22:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0010_postimage_slug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='postimage',
            name='slug',
        ),
    ]
