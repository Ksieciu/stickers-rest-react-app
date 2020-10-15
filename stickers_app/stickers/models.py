from django.conf import settings
from django.db import models
from django.db.models.signals import post_save
from django.utils import timezone
from django.core.exceptions import ObjectDoesNotExist

# Create your models here.

User = settings.AUTH_USER_MODEL


class Board(models.Model):
    owner = models.ForeignKey(User, related_name='boards', on_delete=models.CASCADE)
    name = models.CharField(max_length=50)


class Sticker(models.Model):
    owner = models.ForeignKey(User, related_name='stickers', on_delete=models.CASCADE)
    board = models.ForeignKey(Board, related_name='board_stickers', on_delete=models.CASCADE)
    title = models.CharField(max_length=50, default='', blank=True)
    content = models.TextField(max_length=1000, default='', blank=True)
    checked = models.BooleanField(default=True)
    alert_time = models.DateTimeField(blank=True, null=True)
    creation_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["creation_time"]

    def save(self, *args, **kwargs):
        try:
            print(self.board)
        except ObjectDoesNotExist:
            main_board = Board.objects.get(owner=self.owner, name='Main') or None
            if main_board:
                self.board = main_board

        if self.alert_time:
            self.checked = False
        return super().save(*args, **kwargs)


def user_created(sender, instance, created, *args, **kwargs):
        if created:
            Board.objects.get_or_create(owner=instance, name='Main')

post_save.connect(user_created, sender=User)



