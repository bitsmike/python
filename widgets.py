from Tkinter import *	

class formulario:
	def __init__(self):
		top = Tk()
		lblNumero1 = Label(top)
		lblNumero1["text"]="Primer Numero"
		lblNumero1.pack( side = LEFT)
		txtNumero1 = Entry(top, bd =5)
		txtNumero1.pack(side = RIGHT)
		num1 = txtNumero1.get()
		
		lblNumero2 = Label(top, text="Segundo numero")
		lblNumero2.pack( side = LEFT)
		txtNumero2 = Entry(top, bd =5)
		txtNumero2.pack(side = RIGHT)
		num2 = txtNumero2.get()

		self.btnSumar = Button(top)
		self.btnSumar["text"] = "Sumar"
		self.btnSumar["bg"] = "#f00"
		self.btnSumar["activebackground"] = "#00e"
		self.btnSumar["command"] = self.sumar(num1,num2)
		self.btnSumar.pack(side = RIGHT)

		lblRespuesta = Label(top, text="Respesta: ")
		lblRespuesta.pack( side = LEFT)
		
		top.mainloop()

	def sumar(self, x, y):

		self.x = x
		self.y = y
		respuesta = x + y
		print "hola!!!!!!!1"

crearForm = formulario()