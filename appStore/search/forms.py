from django import forms
from search.models import SearchQuery

class SearchQueryForm(forms.ModelForm):
	query=forms.CharField(max_length=100,help_text='please enter the search query')
	slug=forms.CharField(widget=forms.HiddenInput(),required=False)

	class Meta:
		model=SearchQuery
		fields=('query',)
