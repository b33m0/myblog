# Generated by Django 2.2 on 2021-12-04 19:45

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0010_auto_20211204_1341'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='article',
            options={'ordering': ('-a_created_time',)},
        ),
        migrations.RenameField(
            model_name='article',
            old_name='created_time',
            new_name='a_created_time',
        ),
        migrations.RemoveField(
            model_name='articletopic',
            name='created_time',
        ),
        migrations.AddField(
            model_name='articletopic',
            name='a_created_time',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
