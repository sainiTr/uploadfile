# Generated by Django 4.1 on 2022-09-27 18:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('file', '0002_alter_uploadfile_file_alter_uploadfile_thumb'),
    ]

    operations = [
        migrations.AlterField(
            model_name='uploadfile',
            name='file',
            field=models.FileField(upload_to='media'),
        ),
        migrations.AlterField(
            model_name='uploadfile',
            name='thumb',
            field=models.FileField(upload_to='media'),
        ),
    ]