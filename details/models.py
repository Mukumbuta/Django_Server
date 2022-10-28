from django.db import models

class SlackDetails(models.Model):
    slackUserName = models.CharField(max_length=100)
    backend = models.BooleanField(null=False, blank=False)
    age = models.IntegerField()
    bio = models.TextField()

    def __str__(self):
        return self.slackUserName
