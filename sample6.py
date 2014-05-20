#!/usr/bin/env python
# -*- coding: iso-8859-15 -*-

#
# pygtk
#
# Ejemplo de utilizacion de ScrollBar, Scale y ProgressBar
#
# http://www.lawebdelprogramador.com
#

import pygtk
# Indicamos que deseamos utilizar la versión 2.0 de gtk
pygtk.require('2.0')
import gtk
import gobject

class X(object):
    intervalActivo=False
    def __init__(self):
        # Creamos la ventana. Indicamos que se desea una ventana sometida a las
        # decoraciones y posicionamiento del manejador de ventanas.
        window=gtk.Window(gtk.WINDOW_TOPLEVEL)
        window.set_default_size(300,200)
        window.set_border_width(10)

        window.connect("destroy", self.destroy, None)
        
        # Creamos un contenedor vertical
        vbox=gtk.VBox(False,30)
        
        ##### ScrollBar #####
        # Preparamos el rango para la barra de desplazamiento horizontal
        # El significado de los valores (value=0, lower=0, upper=0, step_incr=0,
        # page_incr=0, page_size=0) es:
        #    value=Valor inicial
        #    lower=Valor minimo
        #    upper=Valor maximo
        #    step_incr=Valor a aumentar o disminuir al pulsar sobre las feclas del scroll
        #    page_incr=Valor a aumentar o disminuir al pulsar sobre la linea del scroll
        adj1=gtk.Adjustment(10,0,100,1,5,0)
        # Creamos la barra de desplazamiento
        self.hscrollbar = gtk.HScrollbar(adj1)
        # Creamos el conector del objeto hscrollbar
        self.hscrollbar.connect("value-changed",self.scrollmove, None)
        self.hscrollbar.show()
        
        # Creamos una etiqueta que mostrar el valor del scrollbar
        self.label=gtk.Label("Value %s" % int(self.hscrollbar.get_value()))
        self.label.show()
        
        # Creamos un contenedor horizontal que contendra el scrollbar y el label
        hbox=gtk.HBox(True,0)
        # Añadimos los widgets
        hbox.pack_start(self.hscrollbar)
        hbox.pack_start(self.label)
        # Mostramos el contenedor horizontal
        hbox.show()
        # Añadimos el contenedor horizontal en el contenedor vertical
        vbox.pack_start(hbox,False)
        
        ##### Scale #####
        # Preparamos el rango...
        adj2=gtk.Adjustment(50,0,100,1,5,0)
        # Creamos la barra horizontal
        hscale=gtk.HScale(adj2)
        # Indicamos que no deseamos ningun decimal
        hscale.set_digits(0)
        # Indicamos la posicion donde deseamos que aparezca el valor. Los valores
        # puden ser: POS_LEFT, POS_RIGHT, POS_TOP(defaul) y POS_BOTTOM
        hscale.set_value_pos(gtk.POS_RIGHT)
        # Mostramos la barra
        hscale.show()
        vbox.pack_start(hscale,False)
        
        ##### ProgressBar #####
        # Creamos la barra de progreso
        self.pbar=gtk.ProgressBar()
        # Mostramos la barra de progreso
        self.pbar.show()
        # Creamos el boton para iniciar la barra de progreso y posteriormente
        # pararla
        self.button=gtk.Button("start")
        # Creamos el conector para que cuando se pulse el boton ejecuta la funcion
        # progressBar_start
        self.button.connect("clicked",self.progressBar_start,None)
        # Mostramos el boton
        self.button.show()
        # Creamos una caja horizontal donde colocaremos la barra de progreso y el
        # boton
        hbox2=gtk.HBox(False,0)
        hbox2.pack_start(self.pbar,True,True,5)
        hbox2.pack_start(self.button)
        hbox2.show()
        
        # Añadimos la caja horizontal en la caja vertical
        vbox.pack_start(hbox2,False)
        # Mostramos el contenedor vertical
        vbox.show()
        
        # Añadimos el contenedor vertical a la ventana
        window.add(vbox)
        window.show()

    # Cada vez que varia el valor del scrollbar, se ejecutara esta funcion
    def scrollmove(self,widget,value=None):
        self.label.set_label("Value %s" % int(self.hscrollbar.get_value()))
    
    # Cada vez que se ejecuta el timeout, llama a esta funcion
    def progressBar_timeout(self,widget,value=None):
        # Aumentamos en 0.01 el valor
        self.value+=0.01
        # Si el valor es igual o superior a 1, finalizamos
        if self.value>=1:
            self.intervalActivo=True
            self.progressBar_start(widget, None)
        else:
            # Los valores a introducir van desde 0.0 a 1.0
            self.pbar.set_fraction(self.value)
        # En el momento que devolvemos False, se cancela el timeout. Si devolvemos
        # True, el timeout continua
        return self.intervalActivo
    
    # Esta funcion se ejecuta cuando pulsamos el boton
    def progressBar_start(self,widget,value=None):
        # Si intervalActivo es True, quiere decir que estamos mostrando la barra
        # de progreso, por lo que la paramos poniendo a False la variable intervalActivo
        if self.intervalActivo:
            self.intervalActivo=False
            # Cambiamos el texto que aparece en la barra de progreso
            self.pbar.set_text("Parado")
            # Cambiamos el texto del boton
            self.button.set_label("start")
        else:
            # Iniciamos la barra de progreso
            self.intervalActivo=True
            # Colocamos el valor a 0 para que empiece nuevamente
            self.value=0
            # Cambiamos el texto que aparece en la barra de progreso
            self.pbar.set_text("En curso")
            # Cambiamos el texto del boton
            self.button.set_label("stop")
            # Iniciamos el temporizador cada 100 milisengundos ejecutara la
            # funcion progressBar_timeout hasta que la misma devuelva False
            self.timer=gobject.timeout_add(100,self.progressBar_timeout,None)

    def destroy(self,widget,value=None):
        # Si no finalizamos el main, puede ser que se nos quede el timeout corriendo
        gtk.main_quit()
        

if __name__=="__main__":
    X()
    gtk.main()
