import csv

from django.core.management.base import BaseCommand
from django.contrib.auth.hashers import make_password

from kefir_api.models import User


class Command(BaseCommand):
    def handle(self, *args, **options):
        with open('data/users.csv', encoding='utf-8') as csvfile:
            spamreader = csv.reader(csvfile)
            for id, row in enumerate(spamreader):
                if id == 0:
                    continue
                User.objects.create(username=row[0],
                                    email=row[1],
                                    password=make_password(row[2]),
                                    is_superuser=row[3],
                                    is_staff=row[4])
