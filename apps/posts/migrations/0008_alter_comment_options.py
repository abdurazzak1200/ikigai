# Generated by Django 3.2.9 on 2022-01-26 07:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0007_alter_category_slug'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comment',
            options={'ordering': ['-commented_time']},
        ),
    ]
