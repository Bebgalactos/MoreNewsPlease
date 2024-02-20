# Generated by Django 5.0 on 2024-02-13 13:17

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Articles', '0001_initial'),
        ('Interactions', '0002_alter_interaction_options_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterField(
            model_name='interaction',
            name='article',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='article_interactions', to='Articles.article'),
        ),
        migrations.AlterField(
            model_name='interaction',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_interactions', to=settings.AUTH_USER_MODEL),
        ),
    ]
