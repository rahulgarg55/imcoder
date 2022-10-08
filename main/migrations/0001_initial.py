# Generated by Django 3.2.8 on 2022-02-03 07:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('person_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=70)),
                ('email', models.EmailField(max_length=254)),
                ('contact', models.CharField(max_length=70)),
                ('desc', models.CharField(max_length=500)),
                ('sub', models.CharField(max_length=500)),
            ],
        ),
    ]
