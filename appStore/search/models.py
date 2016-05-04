from django.db import models
from django.template.defaultfilters import slugify
# Create your models here.


class SearchQuery(models.Model):
	query=models.CharField(max_length=100,unique=True)
	slug=models.SlugField()

	def save(self,*args,**kwargs):
		if self.id is None:
			self.slug=slugify(self.query)
			super(SearchQuery,self).save(*args,**kwargs)

	def __unicode__(self):
		return self.query

class AppInfo(models.Model):
	searchquery=models.ForeignKey(SearchQuery)
	name=models.CharField(max_length=100)
	url=models.CharField(max_length=100)
	developer=models.CharField(max_length=100)
	developer_mailid=models.EmailField()
	icon_url=models.URLField()

	def __unicode__(self):
		return self.app_name