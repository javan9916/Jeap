from django.db import models
from embed_video.fields import EmbedVideoField

class VideoItem(models.Model):
    title = models.CharField(max_length=200)
    video = EmbedVideoField()