# Generated by Django 2.0 on 2019-06-21 00:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0008_post_job_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='price',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True),
        ),
    ]