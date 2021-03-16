import psycopg2 as p
flag = True


PSQL_HOST = "localhost"
PSQL_PORT = "5432"
PSQL_USER = "postgres"
PSQL_PASS = "201801580"
PSQL_DB   = "williamhernandez"

address = """ host=%s port=%s user=%s password=%s dbname=%s 
"""% (PSQL_HOST, PSQL_PORT, PSQL_USER, PSQL_PASS, PSQL_DB)

try:

	connection = p.connect(address)
	cursor = connection.cursor()
	print("¡LA CONEXIÓN CON LA BASE DE DATOS FUE EXITOSA!")

except:

	print("¡NO SE LOGRÓ HACER LA CONEXIÓN CON LA BASE DATOS, INTENTELO NUEVAMENTE!")

while flag == True:

	#try:

	archivo = open("Salida_P02.txt","a")
	print("")
	print("##################################################")
	print("# 1. MOSTRAR LOS DIVISORES DE UN NÚMERO ---- (d) #")
	print("# 2. SALIR ----------------------------------(s) #")
	print("##################################################")
	print("")

	opt = input("INGRESE LA OPCIÓN QUE DESEA EJECUTAR: ")
	print("")

	if opt == "d":

		num = int(input("INGRESE UN NÚMERO ENTERO POSITIVO: "))
		print("")

		divisores = []

		for i in range (1,num+1):
				
			if num%i == 0:
				divisores.append(i)
			else:
				i = i

		print("LOS DIVISORES DE ", num, "SON LOS NÚMEROS:", divisores)
		archivo.write('LOS DIVISORES DEL NÚMERO %s'%(num)+' SON: %s'%divisores+'\n')
		archivo.close()


		SQL = "INSERT INTO divisor(numero,divisores) VALUES ('%s',"'%s'")"
		datos = (num,divisores)
		cursor.execute(SQL,datos)
		connection.commit()

	elif opt == "s":

		flag = False

	else:

		print("######################################")
		print("# USTED NO INGRESO UNA OPCIÓN VALIDA #")
		print("######################################")

	#except:

		#print("USTED NO INGRESO UN NÚMERO ENTERO POSITIVO")

cursor.close()
connection.close()
print("")
print("####################################")
print("# GRACIAS POR UTILIZAR EL PROGRAMA #")
print("####################################") 