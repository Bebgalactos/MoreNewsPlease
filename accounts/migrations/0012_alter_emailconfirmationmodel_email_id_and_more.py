# Generated by Django 5.0 on 2023-12-28 00:40

import datetime
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0011_alter_emailconfirmationmodel_email_id_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='emailconfirmationmodel',
            name='email_id',
            field=models.UUIDField(default=uuid.UUID('0600caac-4ee2-43c5-aac4-37d59614a74d'), primary_key=True, serialize=False, verbose_name='id_email'),
        ),
        migrations.AlterField(
            model_name='emailconfirmationmodel',
            name='expiration_date',
            field=models.DateTimeField(default=datetime.datetime(2023, 12, 28, 1, 40, 32, 282063, tzinfo=datetime.timezone.utc), verbose_name='Expiration Date'),
        ),
    ]