# Generated by Django 2.0.5 on 2018-05-26 17:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('security', '0002_auto_20180526_2250'),
    ]

    operations = [
        migrations.RenameField(
            model_name='securityoffice',
            old_name='Mobile_Num',
            new_name='MobileNumber',
        ),
        migrations.RenameField(
            model_name='securityoffice',
            old_name='Reference',
            new_name='PersonMeeting',
        ),
        migrations.RenameField(
            model_name='securityoffice',
            old_name='Visitor_MailID',
            new_name='VisitorMailID',
        ),
        migrations.RemoveField(
            model_name='securityoffice',
            name='Typeofvisit',
        ),
        migrations.AddField(
            model_name='securityoffice',
            name='Remarks',
            field=models.CharField(default='', max_length=256),
        ),
    ]
