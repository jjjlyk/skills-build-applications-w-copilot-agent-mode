from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Workout, Leaderboard
from django.utils import timezone

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data.'

    def handle(self, *args, **kwargs):
        # Clear existing data
        User.objects.all().delete()
        Team.objects.all().delete()
        Activity.objects.all().delete()
        Workout.objects.all().delete()
        Leaderboard.objects.all().delete()

        # Users
        user1 = User.objects.create(email='alice@merington.edu', name='Alice', password='alicepass')
        user2 = User.objects.create(email='bob@merington.edu', name='Bob', password='bobpass')
        user3 = User.objects.create(email='carol@merington.edu', name='Carol', password='carolpass')

        # Teams (assign member emails, not objects, for ArrayField compatibility)
        team1 = Team.objects.create(name='Merington Tigers', members=[user1.email, user2.email])
        team2 = Team.objects.create(name='Merington Lions', members=[user3.email])

        # Activities
        Activity.objects.create(user=user1, activity_type='run', duration=30, date=timezone.now())
        Activity.objects.create(user=user2, activity_type='walk', duration=60, date=timezone.now())
        Activity.objects.create(user=user3, activity_type='cycle', duration=45, date=timezone.now())

        # Workouts
        Workout.objects.create(user=user1, workout_type='yoga', duration=60, date=timezone.now())
        Workout.objects.create(user=user2, workout_type='swim', duration=30, date=timezone.now())
        Workout.objects.create(user=user3, workout_type='weights', duration=40, date=timezone.now())

        # Leaderboard
        Leaderboard.objects.create(user=user1, score=120, rank=1)
        Leaderboard.objects.create(user=user2, score=100, rank=2)
        Leaderboard.objects.create(user=user3, score=90, rank=3)

        self.stdout.write(self.style.SUCCESS('Test data populated successfully.'))
