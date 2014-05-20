#-*- encoding = utf8 -*-
#importamos modulos
from visual import *
from moduloCaida import *

print "Bienvenido al lanzamiento de un proyectil"
final = False #declarar que todavia no se debe finalizar el programa
#genera donde van a estar los graficos
ventana = display(title="Proyectil", width=1000, height=1000, background=(0,0,0), forward=(0,-1,-1))
while not final:#mientras no sea todavia el final
	rpta = menu()#imprimir menu y devolver la eleccion
	#resetear variables
	altura = 0
	velocidad = 0
	tiempo = 0
	distanciareco = 0
	tiemponecesario = 0
	tamano = 0
	lejania = 0
	velocidadx = 0
	velocidady = 0
	alturamax = 0
	angulo = 0
	if rpta == 1:#si la respuesta es 1
		print
		print "=============================="
		print " PROYECTIL PREPARADO Y LISTO  "
		print "     SE REQUIEREN DATOS:      "
		print "=============================="
		print
		radio=0.5
		j=False
		while not j:
			velocidad=raw_input("Ingrese la fuerza de disparo en m/s......: ")
			j=validarNum(velocidad)
		velocidad=float(velocidad)
		i=False

		while not i:
			angulo=raw_input("Ingrese el angulo del disparo en grados..: ")
			i=validarAngulo(angulo)
		angulo=float(angulo)

		velocidadx=velocidadHorizontal(angulo, velocidad)#calculamos la velocidad horizontal
		velocidady=velocidadVertical(angulo,velocidad)#Calculamos la velocidad vertical
		alturamax=alturaMax(velocidady)#Calculamos la altura maxima
		lejania=lejaniaParabola(angulo, velocidad)#Calculamos la distancia alcanzada
		tiemponecesario=tiempoNecesariopar(lejania, velocidadx, velocidady)#calculamos el tiempo de impacto

		#generar objetos de la ventana
		if not angulo==90:
			piso=box(pos=(0,0,0), size=(lejania*2.5, 0.05, lejania/2.5), color=color.green)
		else:
			piso=box(pos=(0,0,0), size=(10, 0.05, 5), color=color.green)
		bola=sphere(pos=(0, radio, 0), radius=radio, color=color.yellow)
		labelalt=label(pos=(-25,5,0), xoffset=bola.pos.x, yoffset=bola.pos.y, text="Tiro a "+str(angulo)+" grados\n y a "+str(velocidad)+"m/s")
		curva=curve(color=bola.color)

		tiempo=0
		bola.velocity1=vector(velocidadreal(tiemponecesario,velocidadx),0,0)
		bandera=0
		marcadoraltura=False

		#en las primeras 10 repeticiones el proyectil se mueve aunque este sobre el piso
		while bola.pos.y>=piso.size.y and bandera<10:
			bandera+=1
			rate(50)

			distancia1=distanciapar(tiempo, distanciareco, velocidady)
			distanciareco+=distancia1
			bola.velocity=vector(0, distancia1, 0)
			bola.pos=bola.pos+bola.velocity
			bola.pos=bola.pos+bola.velocity1
			curva.append(pos=bola.pos)
			ventana.center=bola.pos
			tiempo+=0.01

		while bola.pos.y-radio >= piso.size.y:
			rate(50)
			distancia1=distanciapar(tiempo, distanciareco, velocidady)
			distanciareco+=distancia1
			bola.velocity=vector(0, distancia1, 0)
			bola.pos=bola.pos+bola.velocity
			bola.pos=bola.pos+bola.velocity1
			curva.append(pos=bola.pos)
			tiempo+=0.01

		if bola.pos.y<piso.pos.y:
			bola.pos.y=piso.pos.y+radio

		#imprimimos los resultados en la consola
		print
		print "==================="
		print "    RESULTADOS     "
		print "==================="
		print "La altura maxima que alcanzo el proyectil fue de: ",str(alturamax)+" metros."
		print "La distancia maxima que alcanzo el proyectil fue de: ",str(lejania)+" metros."
		print "El proyectil se tardo: ",str(tiemponecesario)+" segundos en hacer impacto."

	elif rpta==2:
		final=True
		print "Adios!!"
		exit()
	bola.visible=False
	del bola
	curva.visible=False
	del curva
	labelalt.visible=False
	del labelalt