# Generated by Django 3.2.6 on 2021-09-09 20:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_alter_post_updated'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ['-status']},
        ),
        migrations.AlterField(
            model_name='post',
            name='status',
            field=models.CharField(choices=[('Draft', 'draft'), ('Published', 'published')], default='Draft', max_length=10),
        ),
    ]
