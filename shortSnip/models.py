from django.db import models


class ShortURL(models.Model):
    original_url = models.URLField(unique=True)
    short_code = models.CharField(max_length=15)
