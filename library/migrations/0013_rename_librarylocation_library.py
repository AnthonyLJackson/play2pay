# Generated by Django 3.2.7 on 2021-10-05 14:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0012_auto_20211005_1012'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='LibraryLocation',
            new_name='Library',
        ),
    ]