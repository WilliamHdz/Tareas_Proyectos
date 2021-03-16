flag = True

while flag == True:
	try:

		archivo = open("Salida_P05.txt","a")
		print("")
		print("##############################################################")
		print("# 1. CALCULAR LOS IMPARES DE UN NÚMERO ENTRE 1 Y 100 --- (i) #")
		print("# 2. SALIR --------------------------------------------- (s) #")
		print("# 3. VER EL HISTORIAL ---------------------------------- (h) #")
		print("##############################################################")
		print("")

		opt = input("INGRESE LA OPCIÓN QUE DESEA EJECUTAR: ")
		print("")

		if opt == "i":
			
			conteo = int(0)
			n = int(input("INGRESE UN NÚMERO ENTRE 1 Y 100: "))
			print("")
			impares = []

			for i in range(1,n+1):

				if((i%2) == 0):
					i = i
				else:
					conteo += 1
					impares.append(i)

			print("EL NÚMERO ",n," CONTIENE ",conteo, "NÚMEROS IMPARES EN EL RANGO DE 1 A EL MISMO")
			print("LOS CUALES SON: ",impares)

			archivo.write('EL NÚMERO %s'%(n)+' CONTIENE: %s'%conteo+' NÚMEROS IMPARES EN EL RANGO DE 1 A EL MISMO\n')
			archivo.write('LOS CUALES SON: %s'%impares+'\n')
			archivo.write('\n')
			archivo.close()


		elif opt == "h":

			archivo = open("Salida_P05.txt","r")

			historial = archivo.read()
			archivo.close()

			print(historial)

		elif opt == "s":

			flag = False

		else: 

			print("######################################")
			print("# USTED NO INGRESO UNA OPCIÓN VALIDA #")
			print("######################################")

	except:

		print("USTED NO INGRESÓ UN NÚMERO ENTRE 0 Y 100.")

print("")
print("####################################")
print("# GRACIAS POR UTILIZAR EL PROGRAMA #")
print("####################################")