import wx

class Popup(wx.Frame):
	def __init__(self, msg):
		wx.Frame.__init__(self, None, -1, style=wx.NO_BORDER|wx.FRAME_NO_TASKBAR|wx.STAY_ON_TOP, size=(900,100) )


		panel = wx.Panel(self)
		panel.SetBackgroundColour(wx.BLUE)
		self.quote = wx.StaticText(panel, label=msg, pos=(20, 30))
		self.quote.SetForegroundColour((255,255,255))

		# main timer routine
        	self.timer = wx.Timer(self, -1)
        	self.Bind(wx.EVT_TIMER, self.timer_event, self.timer)
        	self.timer.Start(15000)

		panel.Bind(wx.EVT_LEFT_DOWN, self.click)
		self.quote.Bind(wx.EVT_LEFT_DOWN, self.click)


		self.Show(True)
	def timer_event(self, event):
		self.Close(True)

	def click(self, event):
		self.Close(True)
	
