# Generated by Django 5.0 on 2023-12-27 17:11

import datetime
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0010_alter_usercustomised_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='emailconfirmationmodel',
            name='email_id',
            field=models.UUIDField(default=uuid.UUID('9098e9c8-11a3-47c4-b9ae-35822faf3f30'), primary_key=True, serialize=False, verbose_name='id_email'),
        ),
        migrations.AlterField(
            model_name='emailconfirmationmodel',
            name='expiration_date',
            field=models.DateTimeField(default=datetime.datetime(2023, 12, 27, 18, 11, 34, 896857, tzinfo=datetime.timezone.utc), verbose_name='Expiration Date'),
        ),
    ]