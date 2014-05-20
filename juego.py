#llamada recursivas a metodos
class juego:
	def iniciar(self, intentos=1):
		respuesta = raw_input("de que color es la pulpa de la sandia?")
		if intentos == 3:
			print "se acabaron tus intentos"
		else:
			if respuesta.upper() == "ROJO":
				print "Respuesta Correcta!"
			else:
				print "Error!"
				intentos += 1
				self.iniciar(intentos)
jugar = juego()
jugar.iniciar()