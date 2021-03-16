import psycopg2 as p
flag = True

#Constantes Globales:

PSQL_HOST = "localhost"
PSQL_PORT = "5432"
PSQL_USER = "postgres"
PSQL_PASS = "201801580"
PSQL_DB   = "williamhernandez"

#Dirección:

address = """ host=%s port=%s user=%s password=%s dbname=%s 
"""% (PSQL_HOST, PSQL_PORT, PSQL_USER, PSQL_PASS, PSQL_DB)

try:

	connection = p.connect(address)
	cursor = connection.cursor()
	print("¡LA CONEXIÓN CON LA BASE DE DATOS FUE EXITOSA!")

except:

	print("¡NO SE LOGRÓ HACER LA CONEXIÓN CON LA BASE DATOS, INTENTELO NUEVAMENTE!")

while flag == True:

	try:
		print("")
		print("          CALCULADORA          ")
		print("")
		print("###############################")
		print("#  1. SUMA ------------- (s)  #")
		print("#  2. RESTA ------------ (r)  #")
		print("#  3. MULTIPLICACIÓN --- (m)  #")
		print("#  4. DIVISIÓN --------- (d)  #")
		print("#  5. SALIR ------------ (z)  #")
		print("###############################")
		print("")

		opt = input("ELIJA UNA OPCIÓN: ")
		print("")

		if opt == "s":

			print("###################################")
			print("# USTED SELECCIONO LA OPCIÓN SUMA #")
			print("###################################")
			print("")
			num1 = float(input("INGRESE EL PRIMER NÚMERO: "))
			num2 = float(input("INGRESE EL SEGUNDO NÚMERO: "))
			print("")
			z = num1 + num2
			print("EL RESULTADO DE LA SUMA ES: ", z)
			print("___________________________________")
			print("")

			SQL = "INSERT INTO calculadora(primer_numero,segundo_numero,operacion,resultado) VALUES ('%s','%s','Suma','%s')"
			datos = (num1,num2,z)
			cursor.execute(SQL,datos)
			connection.commit()
			

		elif opt == "r":

			print("####################################")
			print("# USTED SELECCIONO LA OPCIÓN RESTA #")
			print("####################################")
			print("")
			num1 = float(input("INGRESE EL PRIMER NÚMERO: "))
			num2 = float(input("INGRESE EL SEGUNDO NÚMERO: "))
			z = num1 - num2
			print("")
			print("EL RESULTADO DE LA RESTA ES: ", z)
			print("____________________________________")
			print("")

			SQL = "INSERT INTO calculadora(primer_numero,segundo_numero,operacion,resultado) VALUES ('%s','%s','Resta','%s')"
			datos = (num1,num2,z)
			cursor.execute(SQL,datos)
			connection.commit()

		elif opt == "m":

			print("#############################################")
			print("# USTED SELECCIONO LA OPCIÓN MULTIPLICACIÓN #")
			print("#############################################")
			print("")
			num1 = float(input("INGRESE EL PRIMER NÚMERO: "))
			num2 = float(input("INGRESE EL SEGUNDO NÚMERO: "))
			z = num1 * num2
			print("")
			print("EL RESULTADO DE LA MULTIPLICACIÓN ES: ", z)
			print("_____________________________________________")
			print("")

			SQL = "INSERT INTO calculadora(primer_numero,segundo_numero,operacion,resultado) VALUES ('%s','%s','Multiplicacion','%s')"
			datos = (num1,num2,z)
			cursor.execute(SQL,datos)
			connection.commit()

		elif opt == "d":

			print("#######################################")
			print("# USTED SELECCIONO LA OPCIÓN DIVISIÓN #")
			print("#######################################")
			print("")
			num1 = float(input("INGRESE EL PRIMER NÚMERO: "))
			num2 = float(input("INGRESE EL SEGUNDO NÚMERO: "))
			print("")

			if num2 == 0:

				print("LA DIVISIÓN ENTRE 0 NO ES POSIBLE")

			else:

				z = num1 / num2
				print("EL RESULTADO DE LA DIVISIÓN ES: ", z)
				print("_______________________________________")
				print("")

				SQL = "INSERT INTO calculadora(primer_numero,segundo_numero,operacion,resultado) VALUES ('%s','%s','Division','%s')"
				datos = (num1,num2,z)
				cursor.execute(SQL,datos)
				connection.commit()

		elif opt == "z":

			flag = False

		else:

			print("######################################")
			print("# USTED NO INGRESO UNA OPCIÓN VALIDA #")
			print("######################################")

	except:

		print("")
		print("###############################")
		print("# ¡INGRESE UN VALOR NUMERICO! #")
		print("###############################")

cursor.close()
connection.close()
print("#####################################")
print("# GRACICAS POR UTILIZAR EL PROGRAMA #")
print("#####################################")
