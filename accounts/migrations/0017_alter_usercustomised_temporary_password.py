# Generated by Django 5.0.2 on 2024-03-06 08:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0016_alter_usercustomised_temporary_password'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usercustomised',
            name='temporary_password',
            field=models.CharField(default='QqdDb4{Ae-P6', max_length=64, verbose_name='Mot de passe temporaire'),
        ),
    ]