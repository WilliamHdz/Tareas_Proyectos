flag = True

while flag == True:

	archivo = open("Salida_P09.txt","a")
	print("")
	print("###########################################################")
	print("# 1. MOSTRAR LISTA DE NÚMEROS DEL MAYOR AL MENOR ---- (m) #")
	print("# 2. SALIR ------------------------------------------ (s) #")
	print("###########################################################")
	print("")

	opt = input("INGRESE LA OPCIÓN QUE DESEA EJECUTAR: ")
	print("")

	if opt == "m":

		num1 = int(input("INGRESE EL PRIMER NÚMERO: "))
		num2 = int(input("INGRESE EL SEGUNDO NÚMERO: "))
		number = []

		if num2 > num1:

			for i in range(num1,num2+1):
		
				i = (-1*i) + (num1+num2)

				if i > num2:
					break
				
				else:
					number.append(i)

			print(number)
			archivo.write('PARA LOS NUMEROS %s Y %s'%(num2,num1)+' LA LISTA DEL MAYOR AL MENOR ES: %s'%number+'\n')
			archivo.close()

		elif num1 > num2:

			for i in range(num2,num1+1):
		
				i = (-1*i) + (num1+num2)

				if i > num1:
					break
				else:
					number.append(i)

			print(number)
			archivo.write('PARA LOS NUMEROS %s Y %s'%(num1,num2)+' LA LISTA DEL MAYOR AL MENOR ES: %s'%number+'\n')
			archivo.close()

		else: 

			print("LOS NÚMEROS SON IGUALES")



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