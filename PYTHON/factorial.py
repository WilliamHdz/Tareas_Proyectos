flag = True
fact = int(1)

while flag == True:

	
	try:
		
		archivo = open("P_registro.txt","a")
		print("")
		print("       CALCULADORA DE FACTORIAL       ")
		print("")
		print("######################################")
		print("# 1. CALCULAR EL FACTORIAL ----- (f) #")
		print("# 2. SALIR ----------------------(s) #") 
		print("######################################")
		print("")

		opt = input("INGRESE LA OPCIÓN QUE ELIGIÓ: ")
		print("")

		if opt == "f":

			num = int(input("INGRESE EL NÚMERO ENTERO AL CUAL DESEA CALCULAR EL FACTORIAL: "))

			if num == 0:

				fact=1

				print("")
				print("EL FACTORIAL DE ", num, " ES: ", fact)
				archivo.write('EL FACTORIAL DE %s'%num)
				archivo.write(' ES: %s'%fact +'\n')
				archivo.close()

			elif num > 0:

				fact = 1

				for i in range(1,num+1):

					fact *= i 

				print("")
				print(" EL FACTORIAL DE ", num, " ES: ", fact)
				archivo.write('EL FACTORIAL DE %s'%num)
				archivo.write(' ES: %s'%fact +'\n')
				archivo.close()

			else:

				fact = s

		elif opt == "s":

			flag = False

		else: 

			
			print("######################################")
			print("# USTED NO INGRESO UNA OPCIÓN VALIDA #")
			print("######################################")

	except:

		print("")
		print("#######################################")
		print("# ¡INGRESE UN NÚMERO ENTERO POSITIVO! #")
		print("#######################################")

print("#####################################")
print("# GRACICAS POR UTILIZAR EL PROGRAMA #")
print("#####################################")