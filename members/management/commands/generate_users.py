from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from faker import Faker
import random

class Command(BaseCommand):
    help = 'Generate random users with Faker'

    def add_arguments(self, parser):
        parser.add_argument(
            'count',
            type=int,
            help='Number of users to create'
        )

    def handle(self, *args, **kwargs):
        faker = Faker()
        count = kwargs['count']

        for _ in range(count):
            username = faker.user_name()
            email = faker.email()
            first_name = faker.first_name()
            last_name = faker.last_name()
            password = "password123"  # Default password for all generated users

            user = User.objects.create_user(
                username=username,
                email=email,
                first_name=first_name,
                last_name=last_name,
                password=password
            )

            self.stdout.write(self.style.SUCCESS(f"✅ Created user: {username} | Email: {email}"))

        self.stdout.write(self.style.SUCCESS(f"🎉 Successfully created {count} user(s)!"))
