# Generated by Django 4.2 on 2023-04-15 18:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tests', '0012_test_random'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='skill',
            field=models.CharField(default='', max_length=100),
        ),
    ]