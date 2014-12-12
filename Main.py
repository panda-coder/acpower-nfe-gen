#!/usr/bin/python
import wx
from popup import Popup
from configgen import ConfigGen


class MainWindow(wx.Frame):
	def __init__(self, parent, title):
		wx.Frame.__init__(self, parent, title=title, size=(500,500))
		self.InitUI()
		self.Centre()
		self.InitEvents()

	def InitEvents(self):
		self.btnEntrada.Bind(wx.EVT_BUTTON, self.btnEntradaClick)
		self.btnEntradaDes.Bind(wx.EVT_BUTTON, self.btnEntradaDesClick)

		self.btnSefaz.Bind(wx.EVT_BUTTON, self.btnSefazClick)
		self.btnSefazDes.Bind(wx.EVT_BUTTON, self.btnSefazDesClick)

		self.Bind(wx.EVT_MENU, self.OnExit, self.menuExit)
                self.Bind(wx.EVT_MENU, self.OnAbout, self.menuSobre)
		self.Bind(wx.EVT_MENU, self.OnConfig, self.menuConfig)
	
	def InitUI(self):
		self.CreateStatusBar()
		self.filemenu = wx.Menu()
		self.menuConfig = self.filemenu.Append(wx.NewId(), 'Configure...', 'Configura')
		self.menuExit = self.filemenu.Append(wx.ID_EXIT, "&Sair", "Sai do programa")

		self.aboutMenu = wx.Menu()
		self.menuSobre = self.aboutMenu.Append(wx.ID_ABOUT, "Sobre", "Informacoes do programa")
		
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
		self.infoEntrada = wx.StaticBox(panel, label="Servico para monitorir lista da sefaz")
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


		sizer.Add(self.SBoxSEntrada, pos=(10,1), span=(1,30), flag=wx.EXPAND|wx.TOP|wx.LEFT|wx.RIGHT, border=10)
		sizer.Add(self.SBoxEmissaoSefaz, pos=(1,5), span=(1,10), flag=wx.EXPAND|wx.TOP|wx.LEFT|wx.RIGHT, border=10)

		self.config = ConfigGen(self)

		panel.SetSizer(sizer)		
		self.Show(True)

	def OnExit(self, e):
		self.Close(True)

	def OnAbout(self, e):
		dlg = wx.MessageDialog( self, "Um gerenciador de NFE da Acpower", "GereNFEPHP", wx.OK)
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
	def btnSefazDesClick(self, event):
		self.btnSefazDes.Disable()
		self.btnSefaz.Enable()

app = wx.App(True)
frame = MainWindow(None, "Gerenciador NFE Acpower")
#pop.Show(True)
app.MainLoop()