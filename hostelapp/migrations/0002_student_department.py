# Generated by Django 2.2.3 on 2019-07-22 02:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hostelapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='department',
            field=models.CharField(default=None, max_length=60),
            preserve_default=False,
        ),
    ]
