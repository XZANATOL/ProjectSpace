# Generated by Django 3.2.6 on 2021-08-29 20:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_rename_staus_post_status'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='cat',
        ),
        migrations.DeleteModel(
            name='images',
        ),
        migrations.DeleteModel(
            name='post',
        ),
    ]