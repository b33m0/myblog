# Generated by Django 2.2 on 2021-12-04 19:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0014_auto_20211204_1348'),
    ]

    operations = [
        migrations.RenameField(
            model_name='article',
            old_name='topic',
            new_name='a_topic',
        ),
    ]