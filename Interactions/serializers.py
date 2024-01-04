from rest_framework import serializers
from .models import Interaction, INTERACTION_TYPE_CHOICES
from django.core.validators import MinValueValidator , MaxValueValidator

class InteractionSerializer(serializers.ModelSerializer):
    user = serializers.CharField(read_only = True)
    article = serializers.UUIDField(read_only = True)
    class Meta:
        model = Interaction
        fields = ('id', 'user', 'article', 'interaction_type', 'timestamp')


class ReadSerializer(InteractionSerializer):
    interaction_type = serializers.HiddenField(default=INTERACTION_TYPE_CHOICES['READ'])


class OpinionSerializer(InteractionSerializer):
    interaction_type = serializers.HiddenField(default=INTERACTION_TYPE_CHOICES['OPINION'])

    class Meta(InteractionSerializer.Meta):
        model = Interaction
        fields = InteractionSerializer.Meta.fields + ("opinion",)


class RatingInteractionSerializer(InteractionSerializer):
    interaction_type = serializers.HiddenField(default=INTERACTION_TYPE_CHOICES['RATING'])
    rating = serializers.IntegerField(validators = [MinValueValidator(limit_value=1),MaxValueValidator(limit_value=5)])

    class Meta(InteractionSerializer.Meta):
        fields = InteractionSerializer.Meta.fields + ('rating',)
        model = Interaction


class ShareInteractionSerializer(InteractionSerializer):
    interaction_type = serializers.HiddenField(default=INTERACTION_TYPE_CHOICES['SHARE'])

    class Meta(InteractionSerializer.Meta):
        fields = InteractionSerializer.Meta.fields + ('share',)
        model = Interaction


class FavoriteInteractionSerializer(InteractionSerializer):
    interaction_type = serializers.HiddenField(default=INTERACTION_TYPE_CHOICES['FAVORITE'])

    class Meta(InteractionSerializer.Meta):
        fields = InteractionSerializer.Meta.fields
        model = Interaction
