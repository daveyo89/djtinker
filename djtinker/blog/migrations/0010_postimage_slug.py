# Generated by Django 3.1.2 on 2020-10-25 22:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_postimage'),
    ]

    operations = [
        migrations.AddField(
            model_name='postimage',
            name='slug',
            field=models.CharField(blank=True, max_length=60),
        ),
    ]
