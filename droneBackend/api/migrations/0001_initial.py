# Generated by Django 3.2.9 on 2021-12-09 12:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DroneData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=25, null=True)),
                ('reg_id', models.IntegerField(default=0)),
                ('last_seen', models.DateTimeField(null=True)),
                ('first_launch', models.DateTimeField(null=True)),
                ('total_flight_time', models.IntegerField()),
            ],
        ),
    ]
