# Generated by Django 5.0 on 2023-12-30 02:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Interactions', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='interaction',
            options={'ordering': ['-timestamp']},
        ),
        migrations.AlterUniqueTogether(
            name='interaction',
            unique_together=set(),
        ),
    ]