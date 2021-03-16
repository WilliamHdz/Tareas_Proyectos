flag = True

while flag == True:

	archivo = open("Salida_P12.txt","a")
	print("")
	print("###############################################")
	print("# 1. CALCULAR EL PROMEDIO DE 3 NOTAS ---- (p) #")
	print("# 2. HISTORIAL -------------------------- (h) #")
	print("# 3. SALIR ------------------------------ (s) #")
	print("###############################################")
	print("")

	opt = input("INGRESE LA OPCIÓN QUE DESEA EJECUTAR: ")
	print("")

	if opt == "p":
		
		n1 = float(input("INGRESE LA PRIMER NONTA: "))
		n2 = float(input("INGRESE LA SEGUNDA NOTA: "))
		n3 = float(input("INGRESE LA TERCER NOTA: "))
		prom = (n1+n1+n3)/3
		print("")

		if prom >= 60:

			print("EL PROMEDIO ES DE",prom,"POR LO TANTO ESTÁ APROBADO.")
			archivo.write('EL PROMEDIO ES DE %s POR LO TANTO ESTÁ APROBADO.\n'%prom)
			archivo.close()

		else:

			print("EL PROMEDIO ES DE",prom,"POR LO TANTO ESTÁ REPROBADO.")
			archivo.write('EL PROMEDIO ES DE %s POR LO TANTO ESTÁ REPROBADO.\n'%prom)
			archivo.close()

	elif opt == "h":

		archivo = open("Salida_P12.txt","r")
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