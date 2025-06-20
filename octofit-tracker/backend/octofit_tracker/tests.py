from django.test import TestCase
from .models import User, Team, Activity, Workout, Leaderboard

class UserModelTest(TestCase):
    def test_create_user(self):
        user = User.objects.create(email='test@example.com', name='Test User', password='testpass')
        self.assertEqual(user.email, 'test@example.com')

class TeamModelTest(TestCase):
    def test_create_team(self):
        team = Team.objects.create(name='Team A')
        self.assertEqual(team.name, 'Team A')

class ActivityModelTest(TestCase):
    def test_create_activity(self):
        user = User.objects.create(email='test2@example.com', name='Test2', password='testpass')
        activity = Activity.objects.create(user=user, activity_type='run', duration=30, date='2025-06-20T00:00:00Z')
        self.assertEqual(activity.activity_type, 'run')

class WorkoutModelTest(TestCase):
    def test_create_workout(self):
        user = User.objects.create(email='test3@example.com', name='Test3', password='testpass')
        workout = Workout.objects.create(user=user, workout_type='yoga', duration=60, date='2025-06-20T00:00:00Z')
        self.assertEqual(workout.workout_type, 'yoga')

class LeaderboardModelTest(TestCase):
    def test_create_leaderboard(self):
        user = User.objects.create(email='test4@example.com', name='Test4', password='testpass')
        leaderboard = Leaderboard.objects.create(user=user, score=100, rank=1)
        self.assertEqual(leaderboard.rank, 1)
