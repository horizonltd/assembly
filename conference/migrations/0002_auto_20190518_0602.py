# Generated by Django 2.2.1 on 2019-05-18 05:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('conference', '0001_initial'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='agenda',
            unique_together={('event', 'order_of_agenda')},
        ),
    ]