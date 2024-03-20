from django.db import models
from accounts.models import UserCustomised
from Articles.models import Article

# Create your models here.


class Recommendation(models.Model):
    id = models.AutoField(primary_key=True)
    articleList = models.ManyToManyField(Article)
    user = models.ManyToManyField(UserCustomised)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Recommendation at {self.timestamp}"
    