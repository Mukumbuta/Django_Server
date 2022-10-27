from django.db import models

class SlackDetails(models.model):
    slackUserName = models.Charfield(max_length=100)
    backend = models.BooleanField(null=False, blank=False)
    age = models.IntergerField()
    bio = models.TextFiled()
