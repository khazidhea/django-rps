from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass


class Game(models.Model):
    STATUS_CREATED = 'created'
    STATUS_STARTED = 'started'
    STATUS_FINISHED = 'finished'

    STATUS_CHOICES = (
        (STATUS_CREATED, STATUS_CREATED),
        (STATUS_STARTED, STATUS_STARTED),
        (STATUS_FINISHED, STATUS_FINISHED),
    )

    users = models.ManyToManyField(User, related_name='users')
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default=STATUS_CREATED)


class Move(models.Model):
    ROCK = 'rock'
    PAPER = 'paper'
    SCISSORS = 'scissors'

    VALUE_CHOICES = (
        (ROCK, ROCK),
        (PAPER, PAPER),
        (SCISSORS, SCISSORS),
    )

    game = models.ForeignKey('Game', on_delete=models.CASCADE, related_name='moves')
    user = models.ForeignKey('User', on_delete=models.CASCADE, related_name='moves')
    value = models.CharField(max_length=20, choices=VALUE_CHOICES)
