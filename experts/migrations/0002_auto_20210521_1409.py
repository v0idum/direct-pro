# Generated by Django 3.1.7 on 2021-05-21 14:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('experts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='expertprofile',
            name='department',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='expertprofile',
            name='diploma_photo',
            field=models.ImageField(blank=True, upload_to='diplomas/'),
        ),
        migrations.AddField(
            model_name='expertprofile',
            name='institution',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='expertprofile',
            name='passport_photo',
            field=models.ImageField(blank=True, upload_to='passports/'),
        ),
    ]
