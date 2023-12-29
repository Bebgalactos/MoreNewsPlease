# Generated by Django 5.0 on 2023-12-29 17:25

import django.contrib.postgres.fields
import django.db.models.deletion
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Newspaper',
            fields=[
                ('newspaper_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(max_length=50)),
                ('avatar_url', models.URLField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Article',
            fields=[
                ('article_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('title', models.TextField()),
                ('descritpion', models.TextField()),
                ('publication_date', models.DateTimeField()),
                ('image_url', models.URLField(blank=True)),
                ('tags', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=20), default=list, size=10)),
                ('author', models.TextField()),
                ('content', models.TextField()),
                ('newspaper', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Articles.newspaper')),
            ],
        ),
    ]
