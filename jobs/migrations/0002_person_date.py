# Generated by Django 3.1.2 on 2020-10-27 19:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='Date',
            field=models.DateField(default='2020-10-28'),
        ),
    ]