from os import path, listdir
from django.core.cache import cache
from django.conf import settings
from django.core.management import BaseCommand, call_command


class Command(BaseCommand):
    help = "Load all fixture data to database"

    def handle(self, *args, **options):
        dirpath = path.join(settings.BASE_DIR + '/fixtures/')
        fixtures = [f for f in listdir(dirpath) if path.isfile(path.join(dirpath, f))]
        for each_fixture in fixtures:
            print "installing", (each_fixture)
            call_command('loaddata', dirpath + each_fixture)
        cache.clear()
        return 'Success!'
