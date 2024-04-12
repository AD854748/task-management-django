# Generated by Django 5.0.4 on 2024-04-08 16:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('boardstory', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='storymodel',
            name='priority',
            field=models.CharField(choices=[('P1', 'P1'), ('P2', 'P2'), ('P3', 'P3')], max_length=100),
        ),
        migrations.AlterField(
            model_name='storymodel',
            name='status',
            field=models.CharField(choices=[('active', 'Active'), ('inactive', 'Inactive'), ('deleted', 'Deleted')], max_length=10),
        ),
    ]
