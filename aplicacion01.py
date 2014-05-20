# -*- coding: utf-8 -*-

try:
    import wx
    import wx.lib.agw.aquabutton as AB
    import wx.lib.platebtn as platebtn
except ImportError:
    raise ImportError,"El modulo wxPython es requerido para ejecutar este programa"

class simpleapp_wx(wx.Frame):
	#creamos una clase que hereda de wx.Frame
    def __init__(self,parent,id,title):
    	#creamos el METODO metodo constructor
        wx.Frame.__init__(self,parent,id,title)
        #Jerarquia de objetos, creamos una interfaz
        self.parent = parent
        #hacemos un seguimiento de la clase padre
        self.initialize()
        #peticion de inicializacion del metodo initialize()

    def initialize(self):
    	sizer = wx.GridBagSizer()
    	#creamos un layout manager para ubicar nuestros widget

    	self.txtBuscar = wx.TextCtrl(self,-1,value=u"Ej. Amelia Ticona, 143536, etc")
    	self.btnBuscar = wx.Button(self, -1,label="Hello World!")
        self.lblBuscar = wx.StaticText(self,-1, "Buscar: ")
        self.lblBuscar.SetBackgroundColour(wx.BLUE)
        self.lblBuscar.SetForegroundColour(wx.WHITE)
    	#Aqui creamos nuestros widget

    	sizer.Add(self.txtBuscar, (0,1), (1,1), wx.EXPAND)
    	sizer.Add(self.btnBuscar, (0,2))
        sizer.Add(self.lblBuscar, (1,1), (2,2), wx.EXPAND)
        #Agregamos al grid nuestro widget

        sizer.AddGrowableCol(0)
        #añadimos una caracteristica de redimencionar los widget cuando la ventana cambie de tamaño

        self.SetSizerAndFit(sizer)
        #Pone a la ventana al tamaño necesitado por los widget	
        self.Show(True)
        #muestra los widget creados, si esto no se pone en True, no se mostrara nada.

if __name__ == "__main__":
    app = wx.App()
    frame = simpleapp_wx(None,-1,'Mi primera app')
    app.MainLoop()