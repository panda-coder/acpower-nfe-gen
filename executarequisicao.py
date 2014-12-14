#!/usr/bin/python

import ConfigParser, os
try:
	import requests
except ImportError, e:
	print "Requests nao encontrado. Pode instalar via apt-get install python-requests"
	exit() 

class ExecutaRequisicao:
	def __init__(self):
		self.config = ConfigParser.ConfigParser()
		self.config.read('defaults.cfg')

		self.urlEntrada = self.config.get('EntradaSefaz', 'urlprocesso')
		self.urlServiceSefaz = self.config.get('ServiceSefaz', 'urlprocesso')
		self.urlInternal = self.config.get('ServiceInternal', 'urlprocesso')

	def ShowEntradaSefaz(self):
		print self.urlEntrada

	def ExecutaSefaz(self):
		print "Executando sefaz" 
	def ExecutaInterno(self):
		print "Executando interno"

	def ExecutaEntrada(self):
		print requests.get(self.urlEntrada).text

