# Generated by Django 2.2 on 2021-12-04 19:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0008_auto_20211204_1333'),
    ]

    operations = [
        migrations.RenameField(
            model_name='article',
            old_name='title',
            new_name='a_title',
        ),
    ]
