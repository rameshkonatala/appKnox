import requests,sys,webbrowser,bs4
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'appStore.settings')
import django
django.setup()

from search.models import SearchQuery,AppInfo

def add_app(query):
	a=SearchQuery.objects.get_or_create(query=query)[0]
	return a

def add_appinfo(app,app_name,app_id,developer,developer_mailid,icon_url):
	i=AppInfo.objects.get_or_create(searchquery=app)[0]
	i.app_name=app_name
	i.app_id=app_id
	i.developer=developer
	i.developer_mailid=developer_mailid
	i.icon_url=icon_url
	return i

def populate(query):
	applist=appInfo(query)
	for key in applist:
		appinfolist=appDetails(applist[key])
		add_appinfo(query,key,applist[key],appinfolist[0],appinfolist[1],appinfolist[2])


def appDetails(app_url):
  #display text while downloading the Google page
	res=requests.get(app_url)
	res.raise_for_status()
	soup=bs4.BeautifulSoup(res.text,"html.parser")

	app_icon=soup.find('div',{'class':'details-wrapper apps square-cover id-track-partial-impression id-deep-link-item'}).find('img')['src']

	mailid=soup.find('div',{'class':'details-section metadata'}).findAll('a')
	for item in mailid:
		if 'mailto' in item['href']:
			app_developer_mailid=item['href'][7:]

	app_developer=soup.find('a',{'class':'document-subtitle primary'}).text

	return [app_developer,app_developer_mailid,app_icon]


def appInfo(query):
	url='https://play.google.com/store/search?q={}'.format(query)  #display text while downloading the Google page
	res=requests.get(url)
	res.raise_for_status()
	soup=bs4.BeautifulSoup(res.text,"html.parser")
	app_name={}
	for item in soup.findAll('div',{'class':'card no-rationale square-cover apps small'}):
		a_text=item.find('a',{'class':'title'})
		app_name[a_text.text]='https://play.google.com{}'.format(item.find('a')['href'])
	return app_name
