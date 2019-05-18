# Generated by Django 2.2.1 on 2019-05-18 17:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('conference', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='Downloads',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('File_Title', models.CharField(default='', max_length=200)),
                ('File', models.FileField(upload_to='')),
                ('Author', models.CharField(default='', max_length=200)),
                ('Year', models.DateField(default=1994)),
                ('Conference', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='conf', to='conference.Conference')),
            ],
        ),
    ]
