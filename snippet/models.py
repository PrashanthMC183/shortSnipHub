from django.db import models

from django.db import models
import random
import string


class Snippet(models.Model):
    original_content = models.TextField()
    encrypted_content = models.TextField(blank=True, null=True)
    key = models.CharField(max_length=255, blank=True, null=True)

    def save(self, *args, **kwargs):
        # Generate a random string for encrypted_content if not provided
        if not self.encrypted_content:
            self.encrypted_content = ''.join(random.choices(string.ascii_letters + string.digits, k=50))

        super().save(*args, **kwargs)
