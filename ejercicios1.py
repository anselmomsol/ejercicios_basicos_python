#1
print("Hello World!")

#2
hola = "Hello World!"
print(hola)

#3
nombre = input("Ingresa tu nombre ")
edad = input("Ingresa tu edad ")
print(f"""Tu nombre es {nombre} 
y tu edad es {edad}.""")

#4
nombre1 = input("Ingresa tu nombre ")
numero = int(input("Introduzca un número "))
for i in range(numero):
    print(f"{nombre1}")

#5
nombre2 = input("Ingresa tu nombre ")
nombre_list = list(nombre2)
nombre_len = len(nombre_list) 
print(f"El nombre {nombre2} tiene {nombre_len} letras") 

#6

primer_resultado = ((3 + 2) / (2 * 5))
segundo_resultado = primer_resultado ** 2
print(segundo_resultado)

#7

numero_1 = int(input("Introduzca un número: "))
numero_2 = int(input("Introduzca otro número: "))

cociente = numero_1 / numero_2
resto = numero_1 % numero_2

print(f"los numeros introducidos son {numero_1} y {numero_2}, el cociente de su division es {cociente} y el resto es {resto}") 

#8

capital_inicial = int(input("Introduzca su capital inicial $$: "))
interes = int(input("Introduzca el interes a generar: "))
anos = int(input("Introduzca la cantidad de años que quiere invertir: "))

porcentaje = capital_inicial * interes / 100
total = porcentaje*anos
print(f"El interes generado sera de $ {total}")

#9

payasos_cantidad = int(input("Ingrese la cantidad payasos: "))
muñecas_cantidad = int(input("Ingrese la cantidad de muñecas: "))

payasos_peso = payasos_cantidad * 112
muñecas_peso = muñecas_cantidad * 75
peso_total = payasos_peso + muñecas_peso
print(f"El peso total del paquete será de {peso_total}") 

#10

edad_usuario = int(input("Introduzca su edad: "))
if(edad_usuario >= 18):
    print("Usted es mayor de edad")
else:
    print("Usted NO es mayor de edad")

#11

contraseña = "contraseña"
contraseña_correcta = True

while(contraseña_correcta):
    contra_usuario = input("Introduzca la contraseña: ")
    if(contra_usuario ==  contraseña):
        contraseña_correcta = False
        print("Contraseña correcta.")
        break
    print("Contraseña invalida.")

#12

num1 = int(input("Introduzca dividendo: "))
num2 = int(input("Introduzca divisor: "))

if(num1 and num2 != 0):
    result = num1 / num2
    print(result)
else:
    print("No se puede dividir por cero")

#13

numero_entero = int(input("Introduzca un número entero: "))

if(numero_entero % 2 == 0):
    print("El numero es par")
else:
    print("El numero es impar")

#14

condicion = True

while(condicion):
    puntuacion_usuario = float(input("Introduzca la puntuación: "))
    if puntuacion_usuario == 0.0:
        print("La puntuación es inaceptable y la ganancia es cero.")
        condicion = False
    elif puntuacion_usuario == 0.4:
        ganancia = int(0.4 * 100000)
        print(f"La puntuación es aceptable y la ganancia es {ganancia}")
        condicion = False
    elif puntuacion_usuario == 0.6:
        ganancia2 = int(0.6 * 100000)
        print(f"La puntuacion es meritorio y la ganancia es {ganancia2}")
        condicion = False
    elif puntuacion_usuario > 0.6:
        ganancia3 = int(puntuacion_usuario * 100000)
        print(f"La puntuacion es meritorio y la ganancia es de {ganancia3}")
        condicion = False
    else:
        print("La puntuación no es válida.")

#15

condicion = True

while(condicion):
    edad_usuario = int(input("Introduzca su edad: "))
    if edad_usuario < 4:
        print("Usted puede entrar gratis")
        condicion = False
    elif edad_usuario <= 18:
        print("Usted tiene que pagar $500")
        condicion = False
    elif edad_usuario > 18:
        print("Usted tiene que pagar 1000")
        condicion = False

#16

edad_cumplida = int(input("Introduzca su edad: "))
for i in range(edad_cumplida):
    print(f"Usted a cumplido {i + 1} años durante sus {edad_cumplida} años.")

#17

lista = [1,2,3,4,5,6,7,8,9,10]
numero = 1

for num in lista:
    for numero in lista:
        resultado = num * numero
        print(f"{num} X {numero} = {resultado}")
        numero + 1

#18

palabra_introducida = input("Introduce una palabra: ")

indice = len(palabra_introducida) - 1
while(indice != -1):
    print(palabra_introducida[indice])
    indice = indice - 1

#19

frase = input("Introduce una frase: ")
letra = input("Introduce una letra: ")

contador = 0
for i in frase:
    if i == letra:
        contador += 1
print(f"La letra {letra} aparece {contador} veces en la frase {frase}.")

#20

condicion_2 = True
while(condicion_2):
    eco = input("Introduzca algo: ")
    if eco == "salir":
        condicion_2 = False
else:
    print(eco)

#21

asignaturas = ["Matemáticas", "Física", "Química", "Historia", "Lengua"]
largo_lista = len(asignaturas)

for i in range(0,(largo_lista)):
    print(f"Yo estudio {asignaturas[i]}.")

#22

a = [1,2,3]
b = [-1,0,2]

componente_i = a[0]*b[0]

componente_j = a[1]*b[1]

componente_k = a[2] * b[2]

resultado_final = componente_i + componente_j + componente_k
print(f"El producto escalar entre los siguientes vectores es {resultado_final}")

#23

frutas = {
    "banana" : 80,
    "manzana" : 100,
    "pera" : 50,
    "naranja" : 70
}

fruta = input("¿Qué fruta desea? ").lower()
cantidad = float(input("¿Cuánto desea? "))

for y in frutas.keys():
    if y == fruta:
        precio = frutas[fruta] * cantidad
        print(f"El precio de la frutas es $ {precio}")
    else:
        print("No tenemos esa fruta.")
        break

#24

programa_asignaturas = {
    "Matemáticas" : 6,
    "Física" : 4,
    "Química" : 5,
    "Literatura" : 10,
    "Biologia" : 8,
    "Educación Física" : 4
}

creditos_total = 0
for asignatura,creditos in programa_asignaturas.items():
    print(f"La asignatura {asignatura} tiene los siguientes créditos: {creditos}. ")
    creditos_total += creditos
    print(f"El total de creditos es {creditos_total}")

#25


from string import ascii_lowercase

lista_abc =list(ascii_lowercase)

lista_vocales = ["a","e","i","o","u"]

nueva_lista = list(ascii_lowercase)

for letras in lista_abc:
    for letra in lista_vocales:
        if letras == letra:
            nueva_lista.remove(letra)
print(lista_abc)
print(nueva_lista)