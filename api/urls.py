from django.conf.urls import patterns, url

from api.views import SchoolListView, make_scrapy, DependencyListView, RegistryListView, RegistryDetailView

urlpatterns = patterns('',

    url(r'^schools/$', SchoolListView.as_view(), name='api_school_list'),
    url(r'^dependencies/$', DependencyListView.as_view(), name='api_dependency_list'),
    url(r'^registries/$', RegistryListView.as_view(), name='api_registry_list'),
    url(r'^registry/(?P<pk>\d+)/$', RegistryDetailView.as_view(), name='api_registry_detail'),

)
