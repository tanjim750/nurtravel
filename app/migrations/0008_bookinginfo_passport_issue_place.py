# Generated by Django 5.0 on 2023-12-23 13:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_remove_bookinginfo_passport_issue_place_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='bookinginfo',
            name='passport_issue_place',
            field=models.CharField(default='DHAKA', max_length=1000),
        ),
    ]