# Generated by Django 5.0.6 on 2024-05-20 06:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_logincredentials'),
    ]

    operations = [
        migrations.AddField(
            model_name='logincredentials',
            name='email',
            field=models.CharField(default='NO Email', max_length=100),
        ),
    ]
