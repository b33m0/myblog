# Generated by Django 2.2 on 2021-12-04 20:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0021_auto_20211204_1412'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='a_view_count',
            field=models.PositiveIntegerField(default=1),
        ),
    ]
