from django.core.management.base import BaseCommand, CommandError

class Command(BaseCommand):
    help = "Closes the specified poll for voting"
    def handle(self, *args, **options):
        print("IS UP TO YOU")