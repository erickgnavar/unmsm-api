from django.core.management.base import BaseCommand

from api.tasks import ScrapyTask


class Command(BaseCommand):

    def handle(self, *args, **options):
        task = ScrapyTask()
        task.apply()
