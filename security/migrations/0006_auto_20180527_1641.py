# Generated by Django 2.0.5 on 2018-05-27 11:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('security', '0005_securityoffice_datetime'),
    ]

    operations = [
        migrations.AlterField(
            model_name='securityoffice',
            name='user',
            field=models.EmailField(default='', max_length=254),
        ),
    ]
