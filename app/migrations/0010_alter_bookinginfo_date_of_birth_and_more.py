# Generated by Django 5.0 on 2023-12-23 16:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0009_rename_is_liked_booking_is_copied'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookinginfo',
            name='date_of_birth',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='bookinginfo',
            name='passport_expiry_date',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='bookinginfo',
            name='passport_issue_date',
            field=models.TextField(),
        ),
    ]
