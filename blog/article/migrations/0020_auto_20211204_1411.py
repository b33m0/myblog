# Generated by Django 2.2 on 2021-12-04 20:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0019_auto_20211204_1410'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='a_modified_time',
            field=models.DateTimeField(auto_now=True),
        ),
    ]