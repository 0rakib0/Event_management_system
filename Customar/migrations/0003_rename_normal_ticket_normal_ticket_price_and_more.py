# Generated by Django 4.1.4 on 2023-03-11 18:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Customar', '0002_ticket'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ticket',
            old_name='normal',
            new_name='normal_ticket_price',
        ),
        migrations.RenameField(
            model_name='ticket',
            old_name='premium',
            new_name='premium_ticket_price',
        ),
    ]
