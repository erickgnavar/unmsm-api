import json

from django.views.generic import View
from django.http import HttpResponse
from django.shortcuts import get_object_or_404

from api.models import Entity, Registry


class JsonViewMixin(object):
    """
    get_data method should return dict
    """

    def get(self, request, *args, **kwargs):
        return HttpResponse(json.dumps(self.get_data()), mimetype='application/json')


class SchoolListView(JsonViewMixin, View):

    model = Entity

    def get_schools(self):
        return self.model.objects.filter(type=Entity.TYPE_SCHOOL)

    def get_data(self):
        data = []
        for school in self.get_schools():
            data.append({
                'id': school.id,
                'name': school.name,
                'code': school.code
            })
        return data


class DependencyListView(JsonViewMixin, View):

    model = Entity

    def get_dependencies(self):
        return self.model.objects.filter(type=Entity.TYPE_DEPENDENCY)

    def get_data(self):
        data = []
        for dependency in self.get_dependencies():
            data.append({
                'id': dependency.id,
                'name': dependency.name,
                'code': dependency.code
            })
        return data


class RegistryListView(View, JsonViewMixin):

    model = Registry

    def get_data(self):
        data = []
        for registry in self.model.objects.all():
            data.append({
                'id': registry.id,
                'name': registry.name,
                'email': registry.email,
                'position': registry.annex,
                'position': registry.position
            })
        return data


class RegistryDetailView(View, JsonViewMixin):

    model = Registry

    def get_object(self):
        _object = get_object_or_404(self.model, pk=self.kwargs.get('pk', None))
        return _object

    def get_data(self):
        registry = self.get_object()
        return {
            'id': registry.id,
            'name': registry.name,
            'email': registry.email,
            'position': registry.annex,
            'position': registry.position,
            'entity': {
                'name': registry.entity.name,
                'code': registry.entity.code
            }
        }
