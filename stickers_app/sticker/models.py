from django.db import models
from django.utils import timezone

# Create your models here.

class Sticker(models.Model):
    owner = models.ForeignKey('auth.User', related_name='stickers', on_delete=models.CASCADE)
    title = models.CharField(max_length=50, default='', blank=True)
    content = models.TextField(max_length=1000, default='', blank=True)
    checked = models.BooleanField(default=True)
    alert_time = models.DateTimeField(blank=True, null=True)
    creation_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["creation_time"]

    def save(self, *args, **kwargs):
        if self.alert_time:
            self.checked = False
        return super().save(*args, **kwargs)
