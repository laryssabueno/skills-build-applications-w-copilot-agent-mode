from django.db import models

class User(models.Model):
    username = models.CharField(max_length=100, unique=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.username

class Team(models.Model):
    name = models.CharField(max_length=100, unique=True)
    members = models.ManyToManyField(User, related_name='teams')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Activity(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='activities')
    type = models.CharField(max_length=100)
    duration = models.IntegerField()  # Duration in minutes
    calories_burned = models.FloatField()
    date = models.DateField()

    def __str__(self):
        return f"{self.type} by {self.user.username} on {self.date}"

class Leaderboard(models.Model):
    team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='leaderboard_entries')
    points = models.IntegerField()
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.team.name} - {self.points} points"

class Workout(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    duration = models.IntegerField()  # Duration in minutes
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name