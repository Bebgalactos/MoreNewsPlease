from django.db import models
import uuid
# Create your models here.


class Channel(models.Model):
    channel_id = models.UUIDField(primary_key=True, unique=True , default=uuid.uuid4)
    name = models.CharField(max_length=100, blank=False)
    avatar_url = models.URLField()

    class Meta:
        verbose_name_plural = 'Channels'

    def __str__(self):
        return self.name


class Article(models.Model):
    article_id = models.UUIDField(primary_key=True,unique= True, default=uuid.uuid4, editable = False)
    title = models.CharField(max_length=100, blank=False)
    descritpion = models.CharField(max_length=1000)
    publication_date = models.DateTimeField()
    image_url = models.URLField(blank=True)
    channel = models.ForeignKey(Channel, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = 'Articles'

    def __str__(self):
        return self.title
