flag = True

while flag == True:

	try:

		archivo = open("Salida_P06.txt","a")
		print("")
		print("#########################################################################")
		print("# 1. DETERMINAR EL TIPO DE TRIANGULO CON RESPERCTO A SUS LADOS ---- (t) #")
		print("# 2. SALIR -------------------------------------------------------- (s) #")
		print("# 3. HISTORIAL ---------------------------------------------------- (h) #")
		print("#########################################################################")
		print("")

		opt = input("INGRESE LA OPCIÓN QUE DESEA EJECUTAR: ")
		print("")

		if opt == "t":

			l1 = int(input("INGRESE EL PRIMER LADO: "))
			l2 = int(input("INGRESE EL PRIMER LADO: "))
			l3 = int(input("INGRESE EL PRIMER LADO: "))

			if (l1 == l2 and l1 == l3):

				print("EL TRIANGULO CON LADOS ",l1,",",l2,",","Y",l3," ES UN EQUILATERO.")
				archivo.write('EL TRIANGULO CON LADOS  %s, %s Y %s'%(l1,l2,l3)+' ES UN EQUILÁTERO.\n')
				archivo.close()

			elif (l1 == l2 and (l1 != l3 or l2 != l3)) or (l1 == l3 and (l1 != l2 or l2 != l3)) or (l3 == l2 and (l1 != l3 or l1 != l2)):

				print("EL TRIANGULO CON LADOS ",l1,",",l2,",","Y",l3," ES UN ISOSCELES.")
				archivo.write('EL TRIANGULO CON LADOS  %s, %s Y %s'%(l1,l2,l3)+' ES UN ISÓSCELES.\n')
				archivo.close()

			else:

				print("EL TRIANGULO CON LADOS ",l1,",",l2,",","Y",l3," ES UN ESCALENO.")
				archivo.write('EL TRIANGULO CON LADOS  %s, %s Y %s'%(l1,l2,l3)+' ES UN ESCALENO.\n')
				archivo.close()

		elif opt == "h":

			archivo = open("Salida_P06.txt","r")
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

		print("NO INGRESÓ UN NÚMERO VÁLIDO O INGRESÓ UNA LETRA.")

print("")
print("####################################")
print("# GRACIAS POR UTILIZAR EL PROGRAMA #")
print("####################################")