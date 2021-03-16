flag = True

while flag == True:

	try: 

		archivo = open("Salida_P04.txt","a")
		print("")
		print("##############################################################")
		print("# 1. MOSTRAR LA SUMATORIA DESDE 0 HASTA UN NÚMERO n ---- (n) #")
		print("# 2. SALIR --------------------------------------------- (s) #")
		print("##############################################################")
		print("")

		opt = input("INGRESE LA OPCIÓN QUE DESEA EJECUTAR: ")
		print("")

		if opt == "n":
			
			suma = int(0)
			n = int(input("INGRESE UN NÚMERO n: "))

			for i in range(0,n+1):

				suma += i

			print("LA SUMATORIA DEL NÚMERO ",n," ES: ",suma)
			archivo.write('LA SUMATORIA DEL NÚMERO %s'%(n)+' ES: %s'%suma+'\n')
			archivo.close()

		elif opt == "s":

			flag = False

		else: 

			print("######################################")
			print("# USTED NO INGRESO UNA OPCIÓN VALIDA #")
			print("######################################")

	except:

		print("USTED NO INGRESÓ UN NÚMERO ENTERO POSITIVO.")

print("")
print("####################################")
print("# GRACIAS POR UTILIZAR EL PROGRAMA #")
print("####################################")