#1
import wx
class Frame(wx.Frame):
    def __init__(self,superion):
        wx.Frame.__init__(self,parent=superion,title='sum',size=(400,200))
        panel=wx.Panel(self)
        wx.StaticText(panel,label='input n:',pos=(10,10))
        self.inputN=wx.TextCtrl(panel,pos=(150,10))
        wx.StaticText(panel,label='the sum 1~n:',pos=(150,50))
        self.outsum=wx.TextCtrl(panel,pos=(150,50))
        self.btnsum=wx.Button(panel,label='compute',pos=(150,100),size=(50,30))
        self.Bind(wx.EVT_BUTTON,self.f,self.btnsum)
    def f(self,event):
        n=self.inputN.GetValue()
        n=int()
        i=1
        s=0
        for i in range(1,n+1):
            s=s+i
            self.outsum.SetValue(str(s))
if __name__=='__main__':
    app=wx.App()
    frame=Frame(None)
    frame.Show()
    app.MainLoop()