# Generated by Django 3.2.9 on 2022-01-23 17:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0003_auto_20220122_2042'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='slug',
            field=models.SlugField(default=1, max_length=100, unique=True, verbose_name='Slug'),
            preserve_default=False,
        ),
    ]
