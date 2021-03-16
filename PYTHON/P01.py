flag = True


while flag == True:

	try:

		archivo = open("Salida_P01.txt","a")
		print("")
		print("######################################")
		print("# 1. INGRESAR NÚMEROS ---------- (i) #")
		print("# 2. SALIR --------------------- (s) #")
		print("######################################")
		print("")

		opt = input("¿QUE OPCIÓN DESEA EJECUTAR? ")
		print("")		

		if opt == "i":
			
			num1 = int(input("INGRESE EL PRIMER NÚMERO: "))
			num2 = int(input("INGRESE EL SEGUNDO NÚMERO: "))
			num3 = int(input("INGRESE EL TERCER NÚMERO: "))
			
			print("")

			if (num1 > num2 and num1 > num3) and (num1 != num2 and num1 != num3 and num2 != num3):

				print("LA SUMA DE LOS NÚMEROS ES: ", (num1+num2+num3))
				archivo.write('LA SUMA DE LOS NUMEROS %s, %s Y %s'%(num1,num2,num3)+' ES IGUAL A: %s'%(num1+num2+num3)+'\n')
				archivo.close()

			elif (num2 > num1 and num2 > num3) and (num1 != num2 and num1 != num3 and num2 != num3):

				print("LA MULTIPLICACIÓN DE LOS NÚMEROS ES: ",(num1*num2*num3))
				archivo.write('LA MULTIPLICACIÓN DE LOS NUMEROS %s, %s Y %s'%(num1,num2,num3)+' ES IGUAL A: %s'%(num1*num2*num3)+'\n')
				archivo.close()

			elif (num3 > num2 and num3 > num1) and (num1 != num2 and num1 != num3 and num2 != num3):

				print("LA CONCATENACIÓN DE LOS TRES NÚMEROS ES:",(str(num1)+str(num2)+str(num3)))
				archivo.write('LA CONCATENACIÓN DE LOS NUMEROS %s, %s Y %s'%(num1,num2,num3)+' ES IGUAL A: %s'%(str(num1)+str(num2)+str(num3))+'\n')
				archivo.close()

			elif (num1 == num2 and num3 != num1) or (num1 == num3 and num2 != num1) or (num2 == num3 and num1 != num3):

				if num1 == num2:

					print("EL NÚMERO DIFERENTE ES: ", num3);
					archivo.write('DE LOS NUMEROS %s, %s Y %s'%(num1,num2,num3)+' EL NÚMERO DIFERENTE ES: %s'%num3+'\n')
					archivo.close()

				elif num1 == num3:

					print("EL NÚMERO DIFERENTE ES: ", num2);
					archivo.write('DE LOS NUMEROS %s, %s Y %s'%(num1,num2,num3)+' EL NÚMERO DIFERENTE ES: %s'%num2+'\n')
					archivo.close()

				else:

					print("EL NÚMERO DIFERENTE ES: ", num1);
					archivo.write('DE LOS NUMEROS %s, %s Y %s'%(num1,num2,num3)+' EL NÚMERO DIFERENTE ES: %s'%num1+'\n')
					archivo.close()

			else:
				
				print("LOS NÚMEROS SON IGUALES: ",num1,num2,num3)
				archivo.write('LOS NUMEROS %s, %s Y %s'%(num1,num2,num3)+' SON IGUALES'+'\n')
				archivo.close()


		elif opt == "s":

			flag = False

		else:

			print("######################################")
			print("# USTED NO INGRESO UNA OPCIÓN VALIDA #")
			print("######################################")

	except:

		print("USTED NO INGRESO UN NÚMERO ENTERO POSITIVO.")

print("")
print("####################################")
print("# GRACIAS POR UTILIZAR EL PROGRAMA #")
print("####################################") 