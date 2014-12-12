#!/usr/bin/python

import wx

class ConfigGen(wx.Frame):
	def __init__(self, parent):
		wx.Frame.__init__(self, parent, title="Configuracao", size=(500,500), style=wx.CAPTION )
		self.InitUI()
		self.InitEvents()

	def InitEvents(self):
		self.btnOk.Bind(wx.EVT_BUTTON, self.btnOkClick)

	def btnOkClick(self, event):
		self.Hide()

	def InitUI(self):
		self.panel = wx.Panel(self)	
		self.btnOk = wx.Button(self.panel, label="Ok")

#app = wx.App(True)
#frame = ConfigGen(None, "Gerenciador NFE Acpower")
#app.MainLoop()
