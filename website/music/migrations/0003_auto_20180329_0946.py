# Generated by Django 2.0.3 on 2018-03-29 09:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0002_auto_20180329_0940'),
    ]

    operations = [
        migrations.RenameField(
            model_name='song',
            old_name='file_type',
            new_name='file_format',
        ),
    ]
