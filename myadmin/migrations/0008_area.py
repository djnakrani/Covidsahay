# Generated by Django 3.2.5 on 2021-07-16 14:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myadmin', '0007_auto_20210716_0942'),
    ]

    operations = [
        migrations.CreateModel(
            name='Area',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('aname', models.CharField(max_length=30, null=True)),
                ('City', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='myadmin.city')),
            ],
        ),
    ]
