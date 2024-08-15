from django.db import models


class Topic(models.Model):
    """Topic that user studying."""
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """Return string representation of Topic."""
        return self.text
