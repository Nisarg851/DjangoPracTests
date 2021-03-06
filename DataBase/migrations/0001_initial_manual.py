# Generated by Django 3.1.4 on 2021-02-07 17:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Name')),
                ('birth_date', models.CharField(max_length=50, verbose_name='Name')),
                ('email', models.CharField(max_length=50, verbose_name='Name')),
                ('phone', models.CharField(max_length=50, verbose_name='Name')),
                ('gender', models.CharField(default='male', max_length=10, verbose_name='Gender')),
                ('remember_user', models.BooleanField(default=False, verbose_name='Remember User')),
                ('registration_date', models.DateTimeField(verbose_name='Registered on')),
            ],
        ),
    ]
