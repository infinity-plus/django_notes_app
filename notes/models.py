from django.db import models
from django.conf import settings

User = settings.AUTH_USER_MODEL


class Note(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(
        User,
        null=True,
        blank=True,
        on_delete=models.CASCADE,
    )
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
