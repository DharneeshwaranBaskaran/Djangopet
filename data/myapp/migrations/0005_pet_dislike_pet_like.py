# Generated by Django 5.0.6 on 2024-05-29 11:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_pet_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='pet',
            name='dislike',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='pet',
            name='like',
            field=models.IntegerField(default=0),
        ),
    ]
