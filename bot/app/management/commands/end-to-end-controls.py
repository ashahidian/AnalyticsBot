
# file for end-to-end testing
# populate file is also for end-to-end tests

from django.core.management import BaseCommand
from app.models import Entry
from app.management import categories
from app.management import pipeline


class Command(BaseCommand):
    def handle(self, *args, **options):
        all_together_now("volume client x")


# can be adapted for SQL with (distinct) select from table ..
def fill_categories():

    for entry in Entry.objects.all():
        categories.client.append(str(entry.client_name))
        categories.volume.append(str(entry.volume))
        categories.deal_id.append(str(entry.deal_id))
        categories.rank.append(str(entry.rank))
        categories.ev.append(str(entry.ev))


def run_pipeline(question):

    query = pipeline.pipeline(question)
    return query


def get_answer(query):
    answer = Entry.objects.raw(query)
    return answer


def all_together_now(question):
    fill_categories()
    query = run_pipeline(question)
    for q in query:
        print q
        answer = get_answer(q)
        return answer
