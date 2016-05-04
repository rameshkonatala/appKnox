from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from search.models import SearchQuery,AppInfo
from search.forms import SearchQueryForm,AppInfoForm
from search.scrape2 import populate,appInfo,appDetails
# Create your views here.


def search(request):
	
	form = SearchQueryForm(request.POST)
	if form.is_valid():
		form.save(commit=True)
		data=form.cleaned_data
		searchtext=SearchQuery.objects.get(query=data['query'])
		appdict=appInfo(data['query'])
		for key in appdict:
			app=AppInfo.objects.create(searchquery=searchtext)
			app.searchquery=searchtext
			app.name=key
			app.url=appdict[key]
			detailslist=appDetails(appdict[key])
			app.developer=detailslist[0]
			app.developer_mailid=detailslist[1]
			app.icon_url=detailslist[2]
			app.save()

		return HttpResponseRedirect('/search/'+searchtext.slug)

	return render(request,'search/search.html',{'form':form,})


def results(request,searchquery_query_slug):
	context_dict={}
	try:
		searchquery=SearchQuery.objects.get(slug=searchquery_query_slug)
		apps=AppInfo.objects.filter(searchquery=searchquery)
		context_dict['apps']=apps
	except SearchQuery.DoesNotExist:
		pass

	return render(request,'search/results.html',context_dict)


def details(request,app_url):
	context_dict={}
	try:
		app=AppInfo.objects.filter(url=app_url)
		context_dict['app']=app
	except SearchQuery.DoesNotExist:
		pass

	return render(request,'search/details.html',context_dict)
