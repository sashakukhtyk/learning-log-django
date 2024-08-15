from django.db import models


class Topic(models.Model):
    """Topic that user studying."""
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """Return string representation of Topic."""
        return self.text


class Entry(models.Model):
    """Info about a topic"""
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'entries'

    def __str__(self):
        """Return string representation of Entry."""
        return f"{self.text[:50]}"
