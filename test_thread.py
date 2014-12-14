#!/usr/bin/python

import threading, time

def test():
	print "Teste executed"

class MyThread(threading.Thread):
	def __init__(self, *args):
		threading.Thread.__init__(self)
		self.Text = "Hello!"
		self.keeprunning = True

	def setText(self, txt):
		self.Text = txt

	def setFunction(self, func):
		self.func = func

	def stop(self):
		self.keeprunning = False

	def run(self):
		while self.keeprunning:
			print self.Text
			self.func()
			time.sleep(1)

th = MyThread()
th.setFunction(test)
th.start()

t2 = MyThread()
t2.setFunction(test)
t2.setText("ola")
t2.start()

test()

time.sleep(2)
th.stop()
time.sleep(3)
t2.stop()
