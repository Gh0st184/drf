#!/home/django/project_bot/venv/bin/python
from django.contrib.auth.models import User
from django.core.management.base import BaseCommand

from usersapp.models import MyCustomUser


class Command(BaseCommand):

    def handle(self, *args, **options):
        super_user = MyCustomUser.objects.create_superuser(username='admin',
                                                           email='admin@admin.admin',
                                                           password='admin')
        super_user.save()

        users = (
            {'username': 'BorisI',
             'first_name': 'Boris',
             'last_name': 'Ivanov',
             'email': 'boris@ivanov.ru'},
            {'username': 'IvanI',
             'first_name': 'Ivan',
             'last_name': 'Ivanov',
             'email': 'ivan@ivanov.ru'},
            {'username': 'PetrI',
             'first_name': 'Petr',
             'last_name': 'Ivanov',
             'email': 'Petr@ivanov.ru'},
        )

        for user in users:
            my_user = MyCustomUser.objects.create(username=user['username'],
                                                  first_name=user['first_name'],
                                                  last_name=user['last_name'],
                                                  email=user['email'])
            my_user.save()
