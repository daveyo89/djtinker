# Generated by Django 3.1.2 on 2020-10-30 22:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0013_postimage_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postimage',
            name='description',
            field=models.CharField(blank=True, default='', max_length=120),
        ),
    ]
