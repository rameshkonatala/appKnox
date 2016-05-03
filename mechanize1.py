import urllib
from bs4 import BeautifulSoup
import urlparse
import mechanize
url="http://einsteinpapers.press.princeton.edu/"
br=mechanize.Browser()
br.open(url)

br.set_handle_equiv(True)
br.set_handle_gzip(False)
br.set_handle_redirect(True)
br.set_handle_referer(True)
br.set_handle_robots(False)

for link in br.links():
	newurl=urlparse.urljoin(link.base_url,link.url)
	print newurl
