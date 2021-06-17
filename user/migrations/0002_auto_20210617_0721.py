# Generated by Django 3.2.3 on 2021-06-17 07:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fName', models.CharField(max_length=20, null=True)),
                ('lName', models.CharField(max_length=20, null=True)),
                ('mono', models.BigIntegerField(null=True)),
                ('gender', models.CharField(max_length=10, null=True)),
                ('dob', models.CharField(max_length=10, null=True)),
                ('bGrp', models.CharField(max_length=10, null=True)),
                ('email', models.CharField(max_length=30, null=True)),
                ('state', models.CharField(max_length=20, null=True)),
                ('city', models.CharField(max_length=20, null=True)),
                ('area', models.CharField(max_length=20, null=True)),
                ('add', models.CharField(max_length=50, null=True)),
                ('pwd', models.CharField(max_length=50, null=True)),
            ],
        ),
        migrations.AlterField(
            model_name='contact',
            name='email',
            field=models.CharField(max_length=40, null=True),
        ),
        migrations.AlterField(
            model_name='contact',
            name='message',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='contact',
            name='name',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='contact',
            name='subject',
            field=models.CharField(max_length=20, null=True),
        ),
    ]
