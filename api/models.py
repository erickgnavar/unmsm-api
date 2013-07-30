from django.db import models
from django.utils.translation import ugettext as _


class Entity(models.Model):

    TYPE_SCHOOL = 1
    TYPE_DEPENDENCY = 2

    name = models.CharField(
        _(u'Name'),
        max_length=30
    )
    code = models.CharField(
        _(u'Code'),
        max_length=5
    )
    type = models.IntegerField(
        _(u'Type')
    )

    class Meta:
        app_label = 'api'

    def __unicode__(self):
        return '%s : %s' % (self.name, self.code)


class Registry(models.Model):

    entity = models.ForeignKey(
        'Entity',
        related_name='registry_set'
    )
    name = models.CharField(
        _(u'Name'),
        max_length=30
    )
    email = models.EmailField(
        _(u'Email')
    )
    position = models.CharField(
        _(u'Position'),
        max_length=20
    )
    annex = models.CharField(
        _(u'Annex'),
        max_length=10
    )

    class Meta:
        app_label = 'api'

    def __unicode__(self):
        return '%s : %s' % (self.name, self.position)
