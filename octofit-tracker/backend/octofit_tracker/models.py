from djongo import models

class User(models.Model):
    _id = models.ObjectIdField()
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=100)
    password = models.CharField(max_length=128)
    # Add more fields as needed

class Team(models.Model):
    _id = models.ObjectIdField()
    name = models.CharField(max_length=100)
    members = models.ArrayField(model_container=User)

class Activity(models.Model):
    _id = models.ObjectIdField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    activity_type = models.CharField(max_length=100)
    duration = models.IntegerField()
    date = models.DateTimeField()

class Workout(models.Model):
    _id = models.ObjectIdField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    workout_type = models.CharField(max_length=100)
    duration = models.IntegerField()
    date = models.DateTimeField()

class Leaderboard(models.Model):
    _id = models.ObjectIdField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    score = models.IntegerField()
    rank = models.IntegerField()
