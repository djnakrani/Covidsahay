# Generated by Django 3.2.5 on 2021-07-16 09:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myadmin', '0006_city'),
    ]

    operations = [
        migrations.RenameField(
            model_name='city',
            old_name='City',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='state',
            old_name='State',
            new_name='name',
        ),
    ]
