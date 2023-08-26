#Ejercicio numero 4
EdJuan = int(input())
EdAlberto = round(((EdJuan * 2)/3),0)
EdAna = round(((EdJuan * 4)/3),0)
EdMama = round(EdJuan + EdAlberto + EdAna,0)
print('Edad de Alberto: ',EdAlberto)
print('Edad de Juan: ',EdJuan)
print('Edad de Ana: ',EdAna)
print('Edad de la mama: ',EdMama)

#Ejercicio numero 5
suma = 0
x = 20
suma = suma + x
y = 40
x = x+(y**2)
suma = suma + (x/y)
print('El valor de la suma es: ',suma)

#Ejercicio numero 6
Salario_bruto_semana = 48*5000
Retencion_fuente_semana = int(Salario_bruto_semana*0.125)
Salario_neto_semana = Salario_bruto_semana-Retencion_fuente_semana
print('Retencion fuente: ',Retencion_fuente_semana)
print('Salario neto: ',Salario_neto_semana)
print('Salario bruto: ',Salario_bruto_semana)

#Ejercicio numero 7
numero = int(input())
cuadrado = numero**2
cubo = numero**3
print(numero)
print(cuadrado)
print(cubo)

#Ejercicio numero 8
radio = float(input())
area = 3.14159*(radio**2)
longitud = (radio*2)*3.14159
print('El radio es: ',radio)
print('El area es: ',area)
print('La longitud es: ',longitud)