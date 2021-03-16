flag = True

while flag == True:

	archivo = open("Salida_P13.txt","a")
	print("")
	print("####################################################")
	print("# 1. COMPROBAR SI NACÍ EN UN AÑO BISIESTO ---- (a) #")
	print("# 2. HISTORIAL ------------------------------- (h) #")
	print("# 3. SALIR ----------------------------------- (s) #")
	print("####################################################")
	print("")

	opt = input("INGRESE LA OPCIÓN QUE DESEA EJECUTAR: ")
	print("")

	if opt == "a":

		a = int(input("INGRESE EL AÑO EN QUE NACIÓ: "))

		if (a%4) == 0:

			print("USTED NACIÓ EN EL AÑO",a,"EL CUAL ES UN AÑO BISIESTO.")
			archivo.write('USTED NACIÓ EN EL AÑO %s EL CUAL ES UN AÑO BISIENTO.\n'%a)
			archivo.close()

		else:

			print("USTED NACIÓ EN EL AÑO",a,"EL CUAL NO ES UN AÑO BISIESTO.")
			archivo.write('USTED NACIÓ EN EL AÑO %s EL CUAL NO ES UN AÑO BISIENTO.\n'%a)
			archivo.close()

	elif opt == "s":

		flag = False

	elif opt == "h":

		archivo = open("Salida_P13.txt","r")
		historial = archivo.read()
		archivo.close()
		print(historial)

	else:

		print("######################################")
		print("# USTED NO INGRESO UNA OPCIÓN VALIDA #")
		print("######################################")

print("")
print("####################################")
print("# GRACIAS POR UTILIZAR EL PROGRAMA #")
print("####################################")