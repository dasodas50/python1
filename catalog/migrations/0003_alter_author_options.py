# Generated by Django 3.2.9 on 2021-12-04 16:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0002_auto_20211204_1343'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='author',
            options={'ordering': ['-last_name']},
        ),
    ]
