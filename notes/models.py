from django.db import models
from django.contrib.auth.models import User


class Note(models.Model):
    """Note model
    Fields:
        - title: CharField(max_length=255)
        - content: TextField()
        - created_at: DateTimeField(auto_now_add=True)
        - updated_at: DateTimeField(auto_now=True)
        - author: ForeignKey(User)
    """

    title = models.CharField(max_length=100)
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="notes",
    )
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
