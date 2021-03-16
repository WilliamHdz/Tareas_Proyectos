flag = True

while flag == True:

	archivo = open("Salida_P14.txt","a")
	print("")
	print("#################################################################")
	print("# 1. INGRESAR AL CONTROL DE INFORMACIÓN DE GRUPO TAXIS ---- (t) #")
	print("# 2. HISTORIAL -------------------------------------------- (h) #")
	print("# 3. SALIR ------------------------------------------------ (s) #")
	print("#################################################################")
	print("")

	opt = input("INGRESE LA OPCIÓN QUE DESEA EJECUTAR: ")
	print("")

	if opt == "t":

		modelo = int(input("INGRESE EL AÑO DEL MODELO DEL TAXI:" ))
		recorrido = float(input("INGRESE EL RECORRIDO TOTAL DEL TAXI: "))

		if (modelo < 2007 and recorrido > 20):

			print("EL TAXI DEBE RENOVARSE.")
			archivo.write('EL TAXI CON EL NO. DE MODELO %s Y CON RECORRIDO %s DEBE RENOVARSE.\n'%(modelo,recorrido))
			archivo.close()

		elif (modelo >= 2007 and modelo <= 2013) and recorrido > 20000:

			print("EL TAXI DEBE RECIBIR MANTENIMIENTO.")
			archivo.write('EL TAXI CON EL NO. DE MODELO %s Y CON RECORRIDO %s DEBE RECIBIR MANTENIMIENTO.\n'%(modelo,recorrido))
			archivo.close()

		elif (modelo > 2013 and recorrido < 10000):

			print("EL TAXI ESTÁ EN OPTIMAS CONDICIONES.")
			archivo.write('EL TAXI CON EL NO. DE MODELO %s Y CON RECORRIDO %s ESTÁ EN OPTIMAS CONDICIONES.\n'%(modelo,recorrido))
			archivo.close()

		else:

			print("MECANICO.")
			archivo.write('EL TAXI CON EL NO. DE MODELO %s Y CON RECORRIDO %s DEBE SER LLEVADO AL MECANICO.\n'%(modelo,recorrido))
			archivo.close()

	elif opt == "h":

		archivo = open("Salida_P14.txt","r")
		historial = archivo.read()
		archivo.close()
		print(historial)

	elif opt == "s":

		flag = False

	else:

		print("######################################")
		print("# USTED NO INGRESO UNA OPCIÓN VALIDA #")
		print("######################################")

print("")
print("####################################")
print("# GRACIAS POR UTILIZAR EL PROGRAMA #")
print("####################################")