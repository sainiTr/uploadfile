# Generated by Django 4.1 on 2022-09-27 23:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('file', '0007_alter_uploadfile_thumb'),
    ]

    operations = [
        migrations.RenameField(
            model_name='uploadfile',
            old_name='thumb',
            new_name='img',
        ),
    ]
