from django.db import models
import uuid
# Create your models here.


class Newspaper(models.Model):
    newspaper_id = models.UUIDField(
        primary_key=True, unique=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=50)
    avatar_url = models.URLField(max_length=255, blank=False)

    def __str__(self) -> str:
        return self.name


class Article(models.Model):
    article_id = models.UUIDField(
        primary_key=True, unique=True, default=uuid.uuid4, editable=False)
    title = models.TextField(blank=False)
    descritpion = models.TextField(blank=False)
    publication_date = models.DateTimeField(blank=False)
    image_url = models.URLField(blank=True)
    author = models.TextField(blank=False)
    content = models.TextField(blank=False)
    newspaper = models.ForeignKey(Newspaper, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return str(self.title)
