
from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    ADMIN = 'admin'
    COACH = 'coach'
    AGENT = 'agent'
    FOOTBALL_PLAYER = 'football_player'

    ROLE_CHOICES = (
        (ADMIN, 'Admin'),
        (COACH, 'Coach'),
        (AGENT, 'Agent'),
        (FOOTBALL_PLAYER, 'Football Player'),
    )

    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default=FOOTBALL_PLAYER)

    def __str__(self):
        return f"{self.username} ({self.get_role_display()})"