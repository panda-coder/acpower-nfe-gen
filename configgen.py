#!/usr/bin/python

import wx
import ConfigParser
from executarequisicao import ExecutaRequisicao

class ConfigGen(wx.Frame):
	def __init__(self, parent):
		wx.Frame.__init__(self, parent,
				  title="Configuracao",
				  size=(350,350),
				  style=wx.CAPTION )
		self.InitProcess()
		self.InitUI()
		self.InitEvents()
		
	def InitProcess(self):
		self.execReq = ExecutaRequisicao()

	def InitEvents(self):
		self.btnOk.Bind(wx.EVT_BUTTON, self.btnOkClick)

	def btnOkClick(self, event):
		self.SaveConfig()
		self.Hide()

	def InitUI(self):
		self.panel = wx.Panel(self)
		sizer = wx.GridBagSizer(5,5)
		
		sb1 = wx.StaticBox(self.panel, label="Entrada Sefaz")
		self.SBoxSEntrada = wx.StaticBoxSizer(sb1,wx.HORIZONTAL)
		self.EditEntrada = wx.TextCtrl(self.panel,
					       value=self.execReq.getEntrada(),
					       size=(280, -1))
		self.SBoxSEntrada.Add(self.EditEntrada, flag=wx.LEFT)
		
		sb2 = wx.StaticBox(self.panel, label="Servico Sefaz")
		self.SBoxSefaz = wx.StaticBoxSizer(sb2,wx.HORIZONTAL)
		self.EditSefaz = wx.TextCtrl(self.panel,
					       value=self.execReq.getSefaz(),
					       size=(280, -1))
		self.SBoxSefaz.Add(self.EditSefaz, flag=wx.LEFT)
		
		sb3 = wx.StaticBox(self.panel, label="Servico Interno")
		self.SBoxInternal = wx.StaticBoxSizer(sb3,wx.HORIZONTAL)
		self.EditInternal = wx.TextCtrl(self.panel,
					       value=self.execReq.getInternal(),
					       size=(280, -1))
		self.SBoxInternal.Add(self.EditInternal, flag=wx.LEFT)

		self.btnOk = wx.Button(self.panel, label="Ok", pos=(5,200))
		#sizer.Add(self.btnOk, pos=(5,5), span=(1,1),
		#	flag=wx.EXPAND,
		#	border=10)
		sizer.Add(self.SBoxSEntrada, pos=(0,0), span=(1,1),
			  flag=wx.EXPAND|wx.TOP|wx.LEFT|wx.RIGHT,
			  border=10)
		sizer.Add(self.SBoxSefaz, pos=(1,0), span=(1,1),
			  flag=wx.EXPAND|wx.TOP|wx.LEFT|wx.RIGHT,
			  border=10)
		sizer.Add(self.SBoxInternal, pos=(2,0), span=(1,1),
			  flag=wx.EXPAND|wx.TOP|wx.LEFT|wx.RIGHT,
			  border=10)
		self.panel.SetSizer(sizer)

	def SaveConfig(self):
		print "Saving configurations"
		self.execReq.SaveNewConfigs(
			self.EditInternal.GetValue(),
			self.EditSefaz.GetValue(),
			self.EditEntrada.GetValue()
		)
		dlg = wx.MessageDialog( self, "Voce deve reiniciar o programa",
				       "Configuracoes salvas", wx.OK)
		dlg.ShowModal()
		dlg.Destroy()

#app = wx.App(True)
#frame = ConfigGen(None, "Gerenciador NFE Acpower")
#app.MainLoop()
