from django.conf.urls import patterns,url
from search import views

urlpatterns=patterns('',
	url(r'^$',views.search,name='search'),
	url(r'^(?P<searchquery_query_slug>[\w\-]+)/$',views.results,name='results'),
	url(r'^(?P<app_url>[\w\-]+)/$',views.details,name='details'),
	)
