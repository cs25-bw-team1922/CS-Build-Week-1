from django.db import models

# Create your models here.


class User(models.Model):
    first_name = models.TextField(max_length=30)
    last_name = models.TextField(max_length=30)
    user_name = models.CharField(max_length=30)
    password = models.CharField(max_length=30)
    email = models.EmailField(max_length=254).unique()


class Room(models.Model):
    room_name = models.TextField(max_length=30).unique()
    room_description = models.CharField(max_length=1000)
    room_entrance = models.TextField(max_length=30)
    room_exit = models.TextField(max_length=30)


class Character(models.Model):
    character_name = models.TextField(max_length=30)
    character_desc = models.TextField(max_length=1000)
    character_action = models.TextField(max_length=30)
    character_direction = models.TextField(max_length=30)
    character_speaks = models.TextField(max_length=1000)
    character_hackerrank = models.IntegerField(max_length=30)
    character_health = models.IntegerField(max_length=30)
    character_lives = models.IntegerField(max_length=30)
    character_save_stats = models.CharField(max_length=1000)
