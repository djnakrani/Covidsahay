# Generated by Django 3.2.5 on 2021-07-15 19:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myadmin', '0005_state'),
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('City', models.CharField(max_length=30, null=True)),
                ('State', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='myadmin.state')),
            ],
        ),
    ]
