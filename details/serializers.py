from rest_framework import serializers
from details.models import SlackDetails


class SlackDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = SlackDetails
        fields = ['slackUserName', 'backend', 'age', 'bio']