# Generated by Django 3.1.5 on 2021-01-13 06:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('captions', models.CharField(max_length=80)),
                ('photos', models.ImageField(upload_to='sensor_photos')),
            ],
        ),
    ]
