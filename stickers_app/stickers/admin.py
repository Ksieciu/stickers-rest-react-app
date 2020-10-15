from django.contrib import admin
from .models import Sticker, Board
# Register your models here.


class StickerAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'owner', 'checked']
    search_fields = ['checked', 'owner']
    class Meta:
        model = Sticker


admin.site.register(Sticker, StickerAdmin)
admin.site.register(Board)