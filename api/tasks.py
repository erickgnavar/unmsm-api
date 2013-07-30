import urllib
import urllib2

from BeautifulSoup import BeautifulSoup
from celery.task import Task

from api.models import Entity, Registry


class ScrapyTask(Task):

    name = 'school_scrapy_task'
    url = 'http://vicus.unmsm.edu.pe/directorio.asp'

    def run(self):
        print 'Running task'
        for entity in Entity.objects.all():
            self.parse(self.url_to_soap(entity.code), entity)

    def url_to_soap(self, code):
        data = {
            'opttwo': code,
            'submit': 'mostrar'
        }
        data = urllib.urlencode(data)
        request = urllib2.Request(self.url, data=data)
        response = urllib2.urlopen(request)
        soup = BeautifulSoup(response.read(), convertEntities=BeautifulSoup.HTML_ENTITIES)
        return soup

    def parse(self, soup, entity):
        for row in soup.findAll('table')[2].find('table').findAll('tr')[1:]:
            tds = row.findAll('td')
            txt = [td.text for td in tds]
            try:
                data = {
                    'name': txt[0],
                    'annex': txt[1],
                    'position': txt[2],
                    'email': txt[3],
                    'entity': entity
                }
                registry = Registry(**data)
                registry.save()
            except IndexError:
                print txt
