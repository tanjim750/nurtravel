# Generated by Django 5.0 on 2023-12-23 14:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_bookinginfo_passport_issue_place'),
    ]

    operations = [
        migrations.RenameField(
            model_name='booking',
            old_name='is_liked',
            new_name='is_copied',
        ),
    ]
