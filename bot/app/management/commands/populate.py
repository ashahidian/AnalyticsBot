#file for end-to-end testing, to be used with end-to-end-controls.py

from django.core.management import BaseCommand
from app.models import Entry


class Command(BaseCommand):

    def handle(self, *args, **options):
        Entry.objects.all().delete()
        Entry.objects.create(client_name="batatinhas", volume=12.3, deal_id=1, rank=2, ev=10)
        Entry.objects.create(client_name="batatinhas2", volume=123, deal_id=15, rank=7, ev=19)
        Entry.objects.create(client_name="joao", volume=65, deal_id=66, rank=87, ev=135)
        Entry.objects.create(client_name="maria", volume=56, deal_id=88, rank=27, ev=12)
        Entry.objects.create(client_name="joaquina", volume=23, deal_id=9, rank=97, ev=199)
        Entry.objects.create(client_name="luis", volume=9, deal_id=12, rank=99, ev=189)
        Entry.objects.create(client_name="ana", volume=8, deal_id=15, rank=68, ev=9)
        Entry.objects.create(client_name="maca", volume=65, deal_id=9, rank=76, ev=1)
        Entry.objects.create(client_name="marta", volume=456, deal_id=8, rank=58, ev=67)
        Entry.objects.create(client_name="guitarrada", volume=789, deal_id=14536, rank=8, ev=44)
