from django.db import models

# Create your models here.

class Note(models.Model):
    # text
    body = models.TextField()
    #timestamp
    updated = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.body[0:50]

    class Meta:
        ordering = ['-updated']
