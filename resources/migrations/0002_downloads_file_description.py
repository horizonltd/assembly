# Generated by Django 2.2.1 on 2019-05-18 17:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resources', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='downloads',
            name='File_Description',
            field=models.CharField(default='', max_length=200),
        ),
    ]
