# -*- coding: utf-8 -*-
####################################################################
 ###
  ## Un simple script que mejora la eficiencia de convert de ImageMagick para el procesamiento de muchas imágenes.
  ## Sitio web: https://github.com/saulortega/IMconvert
  ## Autor: Saúl Ortega
  ## Versión: 0.1
 ###
####################################################################

import sys
from glob import glob
import os
import shutil
import time
from datetime import datetime


#Hace pausas de un minuto cada 500 imágenes procesadas para evitar sobrecarga del procesador:
descansos=1


reconstruir = u'a'
while not reconstruir.isnumeric():
	reconstruir = input("Cantidad de imágenes a reconstruir:")
	#reconstruir = unicode(str(reconstruir), 'utf-8')

expresion = input("Imágenes a procesar: [*.JPG]")
if expresion == "":
	expresion="*.JPG"

print("Se reconstruirán "+reconstruir+" imágenes intermedias para todas las imágenes que coincidan con la expresión regular '"+str(expresion)+"'.")
input("Pulse una tecla para continuar.")
print("")

lista=glob(expresion)
cantidad=len(lista)
if cantidad == 0:
	print("No se encontraron imágenes que procesar. Asegúrese de haber escrito correctamente el tipo de imágenes a procesar. Si no especifica lo contrario, se buscarán todas las imágenes en el directorio actual con extensión .JPG.")
	sys.exit(0)
if cantidad == 1:
	print("Se necesita al menos dos imágens. Sólo se encontró una.")



try:
	if not os.path.isdir("t"):
		os.mkdir("t")
	else:
		os.rename("t", "tuvwxyz")
		os.mkdir("t")
	if not os.path.isdir("hecho"):
		os.mkdir("hecho")
	else:
		confirma = "a"
		while confirma != "" and confirma != "s" and confirma != "y" and confirma != "si" and confirma != "sí" and confirma != "n" and confirma != "no":
			confirma = input("Existe un directorio llamado 'hecho', el cual se usará para almacenar las imágenes procesadas. ¿Desea continuar sobreescribiendo todo su contenido?")
			confirma = confirma.lower()
		if confirma == "" or confirma == "s" or confirma == "si" or confirma == "sí" or confirma == "y":
			shutil.rmtree("hecho")
			os.mkdir("hecho")
		else:
			print("Elimine o renombre dicho directorio y vuelva a ejecutar este programa.")
			sys.exit(1)
except:
	print("No se pudo crear los directorios de trabajo.")
	sys.exit(1)



inicio = datetime.now()



contador=0
cuenta=0
while contador < (cantidad - 1):
	print("Convirtiendo imagen " + str(contador+1) + ":")
	ejecutar="convert " + lista[0] + " " + lista[1] + " " + "-morph" + " " + str(reconstruir) + " -normalize -monitor t/%d.jpg"
	try:
		os.system(ejecutar)
	except:
		print("Ocurrió un error con la utilidad convert.")
		sys.exit(1)
	
	hechas=glob("t/*.jpg")
	if contador != 0:
		del hechas[0]
	for imagen in hechas:
		try:
			shutil.move(imagen, "hecho/"+str(cuenta)+".jpg")
			cuenta += 1
			if descansos == 1:
				if cuenta%500 == 0:
					print("Descansando...")
					time.sleep(60)
					print("Continúo...")
		except:
			print("Ocurrió un error al intentar transferir las imágenes.")
	
	del lista[0]
	contador += 1



finalizo = datetime.now()


shutil.rmtree("t")
if os.path.isdir("tuvwxyz"):
	os.rename("tuvwxyz", "t")
print("\nProceso finalizado en "+str(finalizo-inicio)+".")
input()
sys.exit(0)
