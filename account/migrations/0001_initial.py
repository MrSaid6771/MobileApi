# Generated by Django 4.1.5 on 2023-01-30 21:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Clent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=255)),
                ('clent_phone_number', models.CharField(blank=True, max_length=255, null=True, unique=True)),
                ('kafil', models.CharField(blank=True, max_length=255, null=True)),
                ('kafil_phone_number', models.CharField(blank=True, default=0, max_length=255, null=True)),
                ('status', models.IntegerField(choices=[(0, 'platinum'), (1, 'blacklist')], default=0)),
            ],
        ),
    ]
