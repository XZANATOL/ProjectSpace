# Generated by Django 3.2.6 on 2021-08-30 21:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_images_post'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name_plural': 'categories'},
        ),
        migrations.AlterModelOptions(
            name='images',
            options={'verbose_name_plural': 'images'},
        ),
        migrations.AddField(
            model_name='images',
            name='title',
            field=models.CharField(default='', max_length=250),
        ),
        migrations.AlterField(
            model_name='images',
            name='image',
            field=models.TextField(),
        ),
    ]