# Generated by Django 5.0.2 on 2024-03-18 15:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0031_alter_usercustomised_temporary_password'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usercustomised',
            name='temporary_password',
            field=models.CharField(default='^{Z^Q&k-zWHP', max_length=64, verbose_name='Mot de passe temporaire'),
        ),
    ]
