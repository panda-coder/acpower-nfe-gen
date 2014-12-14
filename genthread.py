#!/usr/bin/python

import threading, time

class genThread(threading.Thread):
	def __init__(self, *args):
		threading.Thread.__init__(self)
		self.keeprunning = True
		self.func = None
		self.Text = "Hello"

	def setText(self, txt):
		self.Text = txt

	def setFunction(self, func):
		self.func = func

	def stop(self):
		self.keeprunning = False

	def run(self):
		while self.keeprunning:
			print self.Text
			if self.func is not None:
				self.func()
			time.sleep(1)
