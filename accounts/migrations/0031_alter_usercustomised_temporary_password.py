# Generated by Django 5.0.2 on 2024-03-18 15:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0030_alter_usercustomised_temporary_password'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usercustomised',
            name='temporary_password',
            field=models.CharField(default='icIF8cgzCqtC', max_length=64, verbose_name='Mot de passe temporaire'),
        ),
    ]
