# Generated by Django 3.1.1 on 2020-09-17 02:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='last_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
