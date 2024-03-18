# Generated by Django 5.0.2 on 2024-03-18 15:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0027_alter_usercustomised_temporary_password'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usercustomised',
            name='adress',
            field=models.CharField(blank=True, max_length=120, null=True, verbose_name='Adresse'),
        ),
        migrations.AlterField(
            model_name='usercustomised',
            name='last_name',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Nom'),
        ),
        migrations.AlterField(
            model_name='usercustomised',
            name='phone_number',
            field=models.CharField(blank=True, max_length=50, null=True, unique=True, verbose_name='Téléphone'),
        ),
        migrations.AlterField(
            model_name='usercustomised',
            name='temporary_password',
            field=models.CharField(default='Y%&J.K23Hm=.', max_length=64, verbose_name='Mot de passe temporaire'),
        ),
    ]
