# Generated by Django 2.2.3 on 2021-09-26 18:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='users',
            old_name='Deposit_amount',
            new_name='deposit_amount',
        ),
        migrations.RenameField(
            model_name='users',
            old_name='Profession',
            new_name='profession',
        ),
    ]
