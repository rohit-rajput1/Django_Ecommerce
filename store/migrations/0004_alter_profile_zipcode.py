# Generated by Django 5.0.3 on 2024-04-20 09:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0003_profile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='zipcode',
            field=models.IntegerField(),
        ),
    ]
