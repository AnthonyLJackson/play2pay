# Generated by Django 3.2.7 on 2021-10-05 13:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0007_auto_20211005_0937'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='LibraryLocations',
            new_name='LibraryLocation',
        ),
    ]
