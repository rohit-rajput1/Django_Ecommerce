# Generated by Django 5.0.3 on 2024-04-26 13:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0005_profile_country_alter_profile_state_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='date_modified',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
