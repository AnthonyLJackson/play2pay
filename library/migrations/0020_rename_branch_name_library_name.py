# Generated by Django 3.2.7 on 2021-10-05 14:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0019_book_location'),
    ]

    operations = [
        migrations.RenameField(
            model_name='library',
            old_name='branch_name',
            new_name='name',
        ),
    ]