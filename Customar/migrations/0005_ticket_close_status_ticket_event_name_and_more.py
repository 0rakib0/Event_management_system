# Generated by Django 4.1.7 on 2023-03-22 11:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Customar', '0004_wallet'),
    ]

    operations = [
        migrations.AddField(
            model_name='ticket',
            name='close_status',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='ticket',
            name='event_name',
            field=models.CharField(default=1, max_length=150),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='ticket',
            name='event_type',
            field=models.CharField(default=1, max_length=150),
            preserve_default=False,
        ),
    ]
