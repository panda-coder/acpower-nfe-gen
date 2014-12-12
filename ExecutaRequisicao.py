#!/usr/bin/python

import ConfigParser, os
import requests

class ExecutaRequisicao:
	def __init__(self):
		self.config = ConfigParser.ConfigParser()
		self.config.read('defaults.cfg')

		self.urlEntrada = self.config.get('EntradaSefaz', 'urlprocesso')
		#self.urlServiceSefaz = self.config.get('', 'urlprocesso')
		self.urlInternal = self.config.get('ServiceInternal', 'urlprocesso')

	def ShowEntradaSefaz(self):
		print self.urlEntrada

	def ExecutaEntrada(self):
		print requests.get(self.urlEntrada).text

test = ExecutaRequisicao()
test.ExecutaEntrada() 
