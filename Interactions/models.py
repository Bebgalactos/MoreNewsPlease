from email.policy import default
from django.db import models
from django.contrib.auth import get_user_model
from Articles.models import Article
# Create your models here.

INTERACTION_TYPE_CHOICES = {
    "READ": "read",
    "OPINION": "opinion",
    "RATING": "rating",
    "FAVORITE": "favorite",
    "SHARE": "share"
}

OPINION_CHOICES = {
    "LIKE": "like",
    "DISLIKE": "dislike"
}

SHARE_CHOICES = {
    "INSTAGRAM": "instagram",
    "FACEBOOK": "facebook",
    "WHATSAPP": "whatsapp",
    "EMAIL": "email",
    "REDDIT": "reddit"
}


class Interaction(models.Model):
    interaction_type = models.CharField(
        choices=INTERACTION_TYPE_CHOICES, max_length=20, blank=False)
    user = models.ForeignKey(
        get_user_model(), on_delete=models.CASCADE, related_name='user_interactions')
    article = models.ForeignKey(
        Article, on_delete=models.CASCADE, related_name="article_interactions")
    timestamp = models.DateTimeField(auto_now=True)
    rating = models.PositiveSmallIntegerField(null=True, blank=True)
    opinion = models.CharField(
        choices=OPINION_CHOICES, max_length=20, null=True, blank=True)
    share = models.CharField(choices=SHARE_CHOICES,
                             max_length=20, null=True, blank=True)
    duration = models.PositiveSmallIntegerField(null = True , blank = True)

    class Meta:
        ordering = ['-timestamp']
