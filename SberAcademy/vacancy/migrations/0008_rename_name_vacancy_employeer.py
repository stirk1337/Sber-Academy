# Generated by Django 4.2 on 2023-04-16 02:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vacancy', '0007_survey_points'),
    ]

    operations = [
        migrations.RenameField(
            model_name='vacancy',
            old_name='name',
            new_name='employeer',
        ),
    ]