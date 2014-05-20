import math

def menu():
	#esta funcion imprime el menu y devuelve la eleccion
	print """
		1  --> Comenzar el lanzamiento
		2  --> Salir
	"""
	rpta=raw_input("Ingrese su eleccion: ")
	i = True
	#Validar los resultados, que sea una de las elecciones posibles
	while i:
		try:
			rpta = int(rpta)
			if rpta>=1 and rpta<=2:#Revisarmos que la respuesta sea 1 o 2
				i = False#Si cumple sale del Loop
			else:
				print "Opcion incorrecta!"
				rpta = raw_input("Ingrese su eleccion: ")
				i = True
		except:#Si no es un numero, imprimir error y pedir un numero
			i=True
			print "Dato incorrecto, por favor ingresa una opcion"
			rpta = raw_input("Ingrese su eleccion: ")
	return rpta

def distancia(tiempo, distanciareco, velocidad):
	#esta funcion calcula cuanto se debe mover el objeto
	distancia1 = 4.905 * (tiempo ** 2) + velocidad * tiempo
	distanciareal = distancia1 - distanciareco
	return distanciareal

def tiempoReco(distancia):
	tiempo=math.sqrt(distancia/4.905)
	return tiempo

def velocidadreal(tiemponecesario, velocidad):
	factor=tiemponecesario/0.01
	lejania=velocidad*tiemponecesario
	factor2=lejania/factor
	return factor2

def velocidadHorizontal(angulo, velocidad):
	angulorad=(angulo*math.pi)/180
	velocidadx=velocidad*math.cos(angulorad)
	return velocidadx

def velocidadVertical(angulo, velocidad):
	angulorad=(angulo*math.pi)/180
	velocidady=velocidad*math.sin(angulorad)
	return velocidady

def alturaMax(velocidady):
	#esta funcion calcula la altura maxima que se alcanza
	alturamax = 0.5 * ((velocidady ** 2) / 9.81)
	return alturamax

def lejaniaParabola(angulo, velocidad):
	#esta funcion calcula a que distancia caera el proyectil
	angulorad = (angulo*math.pi)/180
	lejania = (2*(velocidad**2)*math.sin(angulorad)*math.cos(angulorad))/9.81
	return lejania

def tiempoNecesario(distancia, velocidad):
	#calcula el tiempo que va a tardar en caer
	tiempo = distancia/velocidad
	return tiempo

def tiempoNecesariopar(distancia, velocidadx, velocidady):
	#tiempo necesario para el proyectil caiga el suelo
	try:
		tiempo = distancia/velocidadx
	except:
		tiempo = (2*velocidady/9.81)#si el angulo fuera de 90 grados, calcular de otra manera
	return tiempo

def distanciapar(tiempo, distanciareco, velocidad):
	#calcular la distancia que sebdebe mover en la parabola
	distancia1=-4.905*(tiempo**2)+velocidad*tiempo
	distanciareal=distancia1 - distanciareco
	return distanciareal

def validarNum(numero):
	try:
		numero=float(numero)
		if numero>0:
			return True
		else:
			print "debe ser un numero positivo"
			return False
	except:
		print "debe ser un numero"
		return False

def  validarAngulo(numero):
	try:
		numero=float(numero)
		if numero>=0 and numero<=90:
			return True
		else:
			print "Debe ser un angulo entre 0 y 90 grados"
			return False
	except:
		print "Debe ser un numero"
		return False