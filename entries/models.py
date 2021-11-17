from django.db import models
from django.utils import timezone
from django.conf import settings
from mdeditor.fields import MDTextField

class Entry(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        default='1',
         )
    title = models.CharField(max_length=200)
    content = MDTextField()
    date_created = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Entries"
