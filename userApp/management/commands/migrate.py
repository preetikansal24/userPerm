from django.core.management import call_command
from django.core.management.commands import migrate


class Command(migrate.Command):
    def handle(self, *args, **options):
        super(Command, self).handle(*args, **options)
        if len(args) == 0:
            call_command('load_fixtures')
            call_command('clearsessions')
