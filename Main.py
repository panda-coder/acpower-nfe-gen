#!/usr/bin/python
import wx
from popup import Popup
from configgen import ConfigGen
from genthread import genThread
from executarequisicao import ExecutaRequisicao

class MainWindow(wx.Frame):
	def __init__(self, parent, title):
		wx.Frame.__init__(self, parent, title=title, size=(500,500))
		self.InitUI()
		self.InitProcess()
		self.InitThreads()
		self.Centre()
		self.InitEvents()

	def InitProcess(self):
		self.execReq = ExecutaRequisicao()

	def InitThreads(self):
		self.InitThreadSefaz()
		self.InitThreadInterno()

	def InitThreadSefaz(self):
		self.ThreadSefaz = genThread()
		self.ThreadSefaz.setFunction(self.execReq.ExecutaSefaz)

	def InitThreadInterno(self):
		self.ThreadInterno = genThread()
		self.ThreadInterno.setFunction(self.execReq.ExecutaInterno)

	def InitEvents(self):
		self.btnEntrada.Bind(wx.EVT_BUTTON, self.btnEntradaClick)
		self.btnEntradaDes.Bind(wx.EVT_BUTTON, self.btnEntradaDesClick)

		self.btnSefaz.Bind(wx.EVT_BUTTON, self.btnSefazClick)
		self.btnSefazDes.Bind(wx.EVT_BUTTON, self.btnSefazDesClick)

		self.btnImpressao.Bind(wx.EVT_BUTTON, self.btnImpressaoClick)
		self.btnImpressaoDes.Bind(wx.EVT_BUTTON, self.btnImpressaoDesClick)

		self.Bind(wx.EVT_MENU, self.OnExit, self.menuExit)
                self.Bind(wx.EVT_MENU, self.OnAbout, self.menuSobre)
		self.Bind(wx.EVT_MENU, self.OnConfig, self.menuConfig)
	
	def InitUI(self):
		self.CreateStatusBar()
		self.filemenu = wx.Menu()
		self.menuConfig = self.filemenu.Append(wx.NewId(),
						       'Configure...', 'Configura')
		self.menuExit = self.filemenu.Append(wx.ID_EXIT, "&Sair", "Sai do programa")

		self.aboutMenu = wx.Menu()
		self.menuSobre = self.aboutMenu.Append(wx.ID_ABOUT,
						       "Sobre", "Informacoes do programa")
		
		self.menuBar = wx.MenuBar()
		self.menuBar.Append(self.filemenu, "&Arquivo")
		self.menuBar.Append(self.aboutMenu, "&Sobre")

		self.SetMenuBar(self.menuBar)

		#self.Bind(wx.EVT_MENU, self.OnExit, menuExit)
		#self.Bind(wx.EVT_MENU, self.OnAbout, menuSobre)

		#wx.NotificationMessage("", "Hello world!").Show()
		panel = wx.Panel(self)
		sizer = wx.GridBagSizer(5,5)

		sb1 = wx.StaticBox(panel, label="Entrada Sefaz")
		self.infoEntrada = wx.StaticBox(panel,
						label="Servico para monitorir lista da sefaz")
		self.SBoxSEntrada = wx.StaticBoxSizer(sb1,wx.HORIZONTAL)
		self.btnEntrada = wx.Button(panel, label="Ativar")
		self.btnEntradaDes = wx.Button(panel, label="Desativar")
		self.btnEntradaDes.Disable()

		self.SBoxSEntrada.Add(self.infoEntrada, flag=wx.LEFT)
		self.SBoxSEntrada.Add(self.btnEntrada, flag=wx.RIGHT)
		self.SBoxSEntrada.Add(self.btnEntradaDes, flag=wx.LEFT)

		sb2 = wx.StaticBox(panel, label="Emissao SEFAZ")
		self.SBoxEmissaoSefaz = wx.StaticBoxSizer(sb2, wx.HORIZONTAL)
		self.btnSefaz = wx.Button(panel, label="Ativar")
		self.btnSefazDes = wx.Button(panel,label="Desativar")
		self.btnSefazDes.Disable()

		self.SBoxEmissaoSefaz.Add(self.btnSefaz, flag=wx.LEFT)
		self.SBoxEmissaoSefaz.Add(self.btnSefazDes, flag=wx.LEFT)

		sb3 = wx.StaticBox(panel, label="Impressao/Interno")
		self.SBoxImpressao = wx.StaticBoxSizer(sb3, wx.HORIZONTAL)
		self.btnImpressao = wx.Button(panel, label="Ativar")
		self.btnImpressaoDes = wx.Button(panel,label="Desativar")
		self.btnImpressaoDes.Disable()
		
		self.SBoxImpressao.Add(self.btnImpressao, flag=wx.LEFT)
		self.SBoxImpressao.Add(self.btnImpressaoDes, flag=wx.LEFT)
		

		sizer.Add(self.SBoxSEntrada, pos=(2,0), span=(1,20),
			  flag=wx.EXPAND|wx.TOP|wx.LEFT|wx.RIGHT,
			  border=10)
		sizer.Add(self.SBoxEmissaoSefaz, pos=(0,0), span=(1,10),
			  flag=wx.EXPAND|wx.TOP|wx.LEFT|wx.RIGHT,
			  border=10)
		sizer.Add(self.SBoxImpressao, pos=(1,0), span=(1,10),
			  flag=wx.EXPAND|wx.TOP|wx.LEFT|wx.RIGHT,
			  border=10)

		self.config = ConfigGen(self)

		panel.SetSizer(sizer)		
		self.Show(True)

	def OnExit(self, e):
		self.Close(True)

	def OnAbout(self, e):
		dlg = wx.MessageDialog( self, "Um gerenciador de NFE da Acpower",
				       "GereNFEPHP", wx.OK)
		dlg.ShowModal()
		dlg.Destroy()
	def OnConfig(self, event):
		self.config.Show()

	def btnEntradaClick(self, event):
		self.btnEntradaDes.Enable()
		self.btnEntrada.Disable()

	def btnEntradaDesClick(self, event):
		self.btnEntrada.Enable()
		self.btnEntradaDes.Disable()
	def btnSefazClick(self, event):
		self.btnSefaz.Disable()
		self.btnSefazDes.Enable()
		self.ThreadSefaz.start()

	def btnSefazDesClick(self, event):
		self.btnSefazDes.Disable()
		self.btnSefaz.Enable()
		self.ThreadSefaz.stop()
		self.InitThreadSefaz()

	def btnImpressaoClick(self, event):
		self.btnImpressaoDes.Enable()
		self.btnImpressao.Disable()
		self.ThreadInterno.start()

	def btnImpressaoDesClick(self, event):
		self.btnImpressao.Enable()
		self.btnImpressaoDes.Disable()
		self.ThreadInterno.stop()
		self.InitThreadInterno()

app = wx.App(True)
frame = MainWindow(None, "Gerenciador NFE Acpower")
#pop.Show(True)
app.MainLoop()
