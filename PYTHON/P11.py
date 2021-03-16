import math as m

flag = True

while flag == True:

	archivo = open("Salida_P11.txt","a")
	print("")
	print("######################################")
	print("# 1. ÁREA DE UN CÍRCULO -------- (c) #")
	print("# 2. ÁREA DE UN TRIÁNGULO ------ (t) #")
	print("# 3. ÁREA DE UN CUADRADO ------- (s) #")
	print("# 4. ÁREA DE UN RECTÁNGULO ----- (r) #")
	print("# 5. HISTORIAL ----------------- (h) #")
	print("# 6. SALIR --------------------- (e) #")
	print("######################################")
	print("")

	opt = input("INGRESE LA OPCIÓN QUE DESEA EJECUTAR: ")
	print("")

	if opt == "c":

		r = float(input("INGRESE EL VALOR DEL RADIO DEL CÍRCULO:"))
		area = (m.pi)*pow(r, 2)
		print("")
		print("EL ÁREA DEL CÍRCULO CON RADIO",r,"ES:",area)
		archivo.write('EL ÁREA DEL CÍRCULO CON RADIO %s'%r+' ES: %s'%area+'\n')
		archivo.close()


	elif opt == "t":

		b = float(input("INGRESE EL VALOR DE LA BASE DEL TRIÁNGULO: "))
		h = float(input("INGRESE EL VALOR DE LA ALTURA DEL TRIÁNGULO: "))
		area = 0.5*b*h
		print("")
		print("EL ÁREA DEL TRIÁNGULO CON BASE",b,"Y ALTURA",h,"ES:",area)
		archivo.write('EL ÁREA DEL TRIÁNGULO CON BASE %s Y ALTURA %s '%(b,h)+' ES: %s'%area+'\n')
		archivo.close()

	elif opt == "s":

		l = float(input("INGRESE EL VALOR DEL LADO DEL CUADRADO: "))
		area = pow(l, 2)
		print("")
		print("EL ÁREA DEL CUADRADO DE LADO",l,"ES:",area)
		archivo.write('EL ÁREA DEL CUADRADO CON LADO %s'%l+' ES: %s'%area+'\n')
		archivo.close()

	elif opt == "r":

		b = float(input("INGRESE EL VALOR DE LA BASE DEL RECTÁNGULO: "))
		h = float(input("INGRESE EL VALOR DE LA ALTURA DEL RECTÁNGULO: "))
		area = b*h
		print("")
		print("EL ÁREA DEL RECTÁNGULO CON BASE",b,"Y ALTURA",h,"ES:",area)
		archivo.write('EL ÁREA DEL RECTÁNGULO CON BASE %s Y ALTURA %s '%(b,h)+' ES: %s'%area+'\n')
		archivo.close()

	elif opt == "h":

		archivo = open("Salida_P11.txt","r")
		historial = archivo.read()
		archivo.close()
		print(historial)		

	elif opt == "e":

		flag = False

	else: 

		print("######################################")
		print("# USTED NO INGRESO UNA OPCIÓN VALIDA #")
		print("######################################")

print("")
print("####################################")
print("# GRACIAS POR UTILIZAR EL PROGRAMA #")
print("####################################")