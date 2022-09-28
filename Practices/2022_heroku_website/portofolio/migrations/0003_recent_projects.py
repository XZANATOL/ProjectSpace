# Generated by Django 3.2.6 on 2021-09-07 20:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portofolio', '0002_auto_20210829_1914'),
    ]

    operations = [
        migrations.CreateModel(
            name='recent_projects',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=300)),
                ('image', models.TextField()),
                ('link', models.URLField(max_length=500)),
            ],
            options={
                'verbose_name_plural': 'recent_projects',
            },
        ),
    ]
