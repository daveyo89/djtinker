# Generated by Django 3.1.2 on 2021-01-10 21:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0016_auto_20210110_1850'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ['-date']},
        ),
    ]
