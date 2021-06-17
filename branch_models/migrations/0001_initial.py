# Generated by Django 3.2.3 on 2021-06-02 07:09

from django_datetime.date_time import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Branch',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('created_date', models.DateField(default=datetime.dnow())),
                ('updated_date', models.DateField(blank=True, null=True)),
                ('is_active', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': 'Branches',
                'verbose_name_plural': 'Branches',
            },
        ),
    ]
