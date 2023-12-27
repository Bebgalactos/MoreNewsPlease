# Generated by Django 5.0 on 2023-12-26 23:47

import datetime
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_alter_emailconfirmationmodel_email_id_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='emailconfirmationmodel',
            name='email_id',
            field=models.UUIDField(default=uuid.UUID('8e00ada1-325e-4903-8c8d-98add58d56da'), primary_key=True, serialize=False, verbose_name='id_email'),
        ),
        migrations.AlterField(
            model_name='emailconfirmationmodel',
            name='expiration_date',
            field=models.DateTimeField(default=datetime.datetime(2023, 12, 27, 0, 47, 54, 399797, tzinfo=datetime.timezone.utc), verbose_name='Expiration Date'),
        ),
    ]
