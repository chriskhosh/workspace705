# Generated by Django 2.0.1 on 2018-02-20 14:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='resume',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.TextField(max_length=255)),
                ('last_name', models.TextField(max_length=255)),
            ],
        ),
    ]
