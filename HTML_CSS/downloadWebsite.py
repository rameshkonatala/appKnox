# -*- coding: utf-8 -*-
import requests,sys,webbrowser,bs4,os

def main():
	URL=str(raw_input('Enter URL : '))
	fileName=URL[55:len(URL)-11]
	print('Converting....  {}').format(fileName)
	os.system('wget --no-check-certificate ‐‐page-requisites ‐‐span-hosts ‐‐convert-links ‐‐adjust-extension {} -O C:\Users\konat\Desktop\codecademy\AngularJS/{}.html'.format(URL,fileName))

while(raw_input()!='0'):
	main()