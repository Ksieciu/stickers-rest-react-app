# Generated by Django 3.1.2 on 2020-10-15 09:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stickers', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sticker',
            name='board',
        ),
    ]
