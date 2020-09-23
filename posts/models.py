from django.db import models

class Post(models.Model):
    subject = models.CharField(max_length=100, null=False, blank=False)
    body = models.TextField(null=False, blank=True)
    likes = models.PositiveIntegerField(null=False, default=0)
