from django.conf.urls import patterns,url
from search import views

urlpatterns=patterns('',
	url(r'^$',views.search,name='search'),
	url(r'^search/(?P<searchquery_query_slug>[\w\-]+)/$',views.results,name='results'),
	)
