flag = True

while flag == True:

	archivo = open("Salida_P07.txt","a")
	print("")
	print("####################################################################")
	print("# 1. CALCULAR EL FACTORIAL DE UN NÚMERO DIVISIBLE ENTRE 7 ---- (f) #")
	print("# 2. HISTORIAL ----------------------------------------------- (h) #")
	print("# 3. SALIR --------------------------------------------------- (s) #")
	print("####################################################################")
	print("")

	opt = input("INGRESE LA OPCIÓN QUE DESEA EJECUTAR: ")
	print("")

	if opt == "f":

		fact = int(1)
		num = int(input("INGRESE UN NÚMERO DIVISIBLE ENTRE 7: "))

		if (num%7) == 0:

			for i in range(1,num+1):
				fact *= i

			print("EL FACTORIAL DE",num,"ES:",fact)
			archivo.write('EL FACTORIAL DE  %s'%num+' ES: %s'%fact+'\n')
			archivo.close() 

		else:

			print("¡ERROR! EL NÚMERO",num,"NO ES DIVISIBLE ENTRE 7.")
			archivo.write('EL NÚMERO  %s'%num+' NO ES DIVISIBLE ENTRE 7.\n')
			archivo.close()

	elif opt == "h":

			archivo = open("Salida_P07.txt","r")
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