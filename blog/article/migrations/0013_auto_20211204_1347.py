# Generated by Django 2.2 on 2021-12-04 19:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0012_auto_20211204_1345'),
    ]

    operations = [
        migrations.RenameField(
            model_name='article',
            old_name='updated_time',
            new_name='a_modified_time',
        ),
    ]
