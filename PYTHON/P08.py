flag = True

while flag == True:

	archivo = open("Salida_P08.txt","a")
	print("")
	print("##############################################################################################")
	print("# 1. MOSTRAR LOS NÚMEROS DE 2 EN 2 DESDE EL NÚMERO DE INICIO HASTA EL NÚMERO DE FIN ---- (f) #")
	print("# 2. SALIR ----------------------------------------------------------------------------- (s) #")
	print("##############################################################################################")
	print("")

	opt = input("INGRESE LA OPCIÓN QUE DESEA EJECUTAR: ")
	print("")

	if opt == "f":

		num1 = int(input("INGRESE EL NÚMERO DE INICIO: "))
		num2 = int(input("INGRESE EL NÚMERO DE FIN: "))
		number = []

		for i in range(num1,num2+1):
	
			i = (2*i) - num1

			if i > num2:
				break
			else:
				number.append(i)

		print(number)
		archivo.write('PARA LOS NUMEROS %s, %s'%(num1,num2)+' SE TIENE: %s'%number+'\n')
		
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