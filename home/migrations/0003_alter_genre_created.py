# Generated by Django 4.2.4 on 2023-09-02 16:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_rename_created_at_genre_created'),
    ]

    operations = [
        migrations.AlterField(
            model_name='genre',
            name='created',
            field=models.DateTimeField(),
        ),
    ]
