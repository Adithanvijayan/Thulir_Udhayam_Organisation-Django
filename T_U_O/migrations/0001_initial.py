# Generated by Django 3.0.8 on 2020-07-18 15:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Members',
            fields=[
                ('email', models.UUIDField(editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=250)),
                ('number', models.CharField(max_length=20)),
                ('pin', models.CharField(max_length=20)),
            ],
        ),
    ]
