#!/usr/bin/python
import requests

site = requests.get("https://bancocn.com.br/")
status = site.status_code

if (status == 200):
	print ("Pagina Existe")
else:
	print ("Pagina Inexistente")
