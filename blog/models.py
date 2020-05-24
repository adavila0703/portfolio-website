from django.db import models

class Blog(models.Model):
    objects = None
    title = models.CharField(max_length=100)
    date = models.DateField(editable=True)
    post = models.TextField(max_length=5000)

    def __str__(self):
        return self.title
