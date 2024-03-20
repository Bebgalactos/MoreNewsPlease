# Generated by Django 5.0.2 on 2024-03-18 20:21

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Articles', '0002_category_article_categories'),
        ('recommendations', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterField(
            model_name='recommendation',
            name='articleList',
            field=models.ManyToManyField(to='Articles.article'),
        ),
        migrations.AlterField(
            model_name='recommendation',
            name='user',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL),
        ),
    ]
