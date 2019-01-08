#1
import wx
class Frame(wx.Frame):
    def __init__(self,superion):
        wx.Frame.__init__(self,parent=superion,title='sum',size=(400,200))
        panel=wx.Panel(self)
        wx.StaticText(panel,label='input n:')