# Generated by Django 4.2.10 on 2024-03-16 22:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('groups', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='group',
            name='AdminID',
            field=models.IntegerField(),
        ),
    ]
