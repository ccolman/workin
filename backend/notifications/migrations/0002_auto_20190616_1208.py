# Generated by Django 2.0.9 on 2019-06-16 12:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notifications', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notification',
            name='verb',
            field=models.CharField(choices=[('L', 'liked'), ('C', 'commented'), ('F', 'cavorited'), ('FL', 'started to follow you'), ('A', 'answered'), ('W', 'accepted'), ('E', 'edited'), ('K', 'also commented'), ('I', 'logged in'), ('O', 'logged out'), ('V', 'voted on'), ('S', 'shared'), ('U', 'created an account'), ('R', 'replied to')], max_length=255),
        ),
    ]