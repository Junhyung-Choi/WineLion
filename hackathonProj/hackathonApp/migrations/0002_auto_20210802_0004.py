# Generated by Django 3.2.2 on 2021-08-02 00:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hackathonApp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='review',
            old_name='user_id',
            new_name='referring_user_id',
        ),
        migrations.RenameField(
            model_name='review',
            old_name='wine_id',
            new_name='referring_wine_id',
        ),
    ]
