import csv

from django.core.management.base import BaseCommand
from datetime import datetime
from phones.models import Phone


class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument('file')

    def handle(self, *args, **options):
        filename = options['file']
        with open(filename, 'r') as csvfile:

            phone_reader = csv.DictReader(csvfile, delimiter=';')

            for line in phone_reader:
                phone = Phone()
                phone.id = line['id']
                phone.name = line['name']
                phone.price = line['price']
                phone.image = line['image']
                phone.release_date = datetime.strptime(line['release_date'], '%Y-%m-%d').date()
                phone.lte_exists = bool(line['lte_exists'])
                phone.save()
