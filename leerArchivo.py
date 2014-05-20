# -*- coding: utf-8 -*-
import os
class documento:
	def __init__(self, nombreArchivo="ejemplo.txt"):
		rutaActual = os.getcwd()
		print rutaActual
		print nombreArchivo
		with open(nombreArchivo, "r") as archivo:
			contenido = archivo.read()
		print contenido
doc1 = documento()