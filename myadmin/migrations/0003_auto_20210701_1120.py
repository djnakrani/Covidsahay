# Generated by Django 3.2.5 on 2021-07-01 11:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myadmin', '0002_rename_admin_myadmin'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='myadmin',
            name='fName',
        ),
        migrations.AddField(
            model_name='myadmin',
            name='aEmail',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='myadmin',
            name='aName',
            field=models.CharField(max_length=30, null=True),
        ),
    ]
