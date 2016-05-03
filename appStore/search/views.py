from django.shortcuts import render
from django.http import HttpResponse
from search.forms import SearchQueryForm
from search.scrape2 import populate 
# Create your views here.


def search(request):
	
	form = SearchQueryForm(request.POST)
	if form.is_valid():
		form.save(commit=True)
		data=form.cleaned_data
		populate(data['query'])


	return render(request,'search/search.html',{'form':form})


def results(request,searchquery_query_slug):
	context_dict={}
	try:
		searchquery=SearchQuery.objects.get(slug=searchquery_query_slug)
		context_dict['app_name']=searchquery.app_name
		context_dict['app_id']=searchquery.app_id
	except SearchQuery.DoesNotExist:
		pass

	return render(request,'search/results.html',context_dict)
