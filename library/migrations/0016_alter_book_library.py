# Generated by Django 3.2.7 on 2021-10-05 14:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0015_book_library'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='library',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='library.library'),
        ),
    ]
