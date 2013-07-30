from django.core.management.base import BaseCommand

from api.models import Entity


class Command(BaseCommand):

    def handle(self, *args, **options):
        if not Entity.objects.filter(type=Entity.TYPE_DEPENDENCY).count():
            print 'Inserting dependencies'
            with open('dependencies.txt') as dep:
                for line in dep.readlines():
                    name = line.split('-')[0].replace('\'', '').replace('\n', '')
                    code = line.split('-')[1].replace('\'', '').replace('\n', '')
                    if code != '' and name != '':
                        entity = Entity(
                            name=name,
                            code=code,
                            type=Entity.TYPE_DEPENDENCY
                        )
                        entity.save()
        else:
            print 'dependencies already inserted'
        if not Entity.objects.filter(type=Entity.TYPE_SCHOOL).count():
            print 'Inserting schools'
            with open('schools.txt') as dep:
                for line in dep.readlines():
                    name = line.split('-')[0].replace('\'', '').replace('\n', '')
                    code = line.split('-')[1].replace('\'', '').replace('\n', '')
                    if code != '' and name != '':
                        entity = Entity(
                            name=name,
                            code=code,
                            type=Entity.TYPE_SCHOOL
                        )
                        entity.save()
        else:
            print 'schools already inserted'
