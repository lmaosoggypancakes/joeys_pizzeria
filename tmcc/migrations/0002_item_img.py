# Generated by Django 3.1.2 on 2020-11-23 19:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tmcc', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='img',
            field=models.URLField(null=True),
        ),
    ]
