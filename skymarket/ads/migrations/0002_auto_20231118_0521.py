# Generated by Django 3.2.6 on 2023-11-18 02:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ads', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ad',
            old_name='owner',
            new_name='author',
        ),
        migrations.RenameField(
            model_name='comment',
            old_name='owner',
            new_name='author',
        ),
    ]
