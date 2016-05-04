from django import forms
from search.models import SearchQuery,AppInfo

class SearchQueryForm(forms.ModelForm):
	query=forms.CharField(max_length=100,help_text='please enter the search query')
	slug=forms.CharField(widget=forms.HiddenInput(),required=False)

	class Meta:
		model=SearchQuery
		fields=('query',)

class AppInfoForm(forms.ModelForm):
	app_name=forms.CharField(max_length=100)
	app_id=forms.CharField(max_length=100)
	developer=forms.CharField(max_length=100)
	developer_mailid=forms.EmailField()
	icon_url=forms.URLField()

	class Meta:
		model=AppInfo
		exclude=('searchquery',)